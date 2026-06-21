#!/usr/bin/env python3
"""
Soul Manteca — Generador de imágenes de producto (vintage streetwear).

Toma una foto de referencia de una prenda (./referencia/reebok.jpeg) y recrea,
mediante imagen-a-imagen, a una persona caminando por una calle urbana de Buenos
Aires con ESE MISMO conjunto puesto. Usa dos motores y guarda las salidas en
./salidas/ con nombres distintos:

  1) Google Gemini  -> modelo "gemini-3.1-flash-image-preview" (Nano Banana 2)
                       vía generateContent del SDK `google-genai`.
                       La imagen se pasa como inline_data + prompt de texto.
                       Requiere GEMINI_API_KEY.

  2) OpenAI         -> modelo "gpt-image-2" vía endpoint /v1/images/edits
                       (la referencia se sube como archivo). Tamaño 1024x1536.
                       Requiere OPENAI_API_KEY.

Dependencias:
    pip install google-genai requests

Uso:
    export GEMINI_API_KEY="..."
    export OPENAI_API_KEY="..."
    python generar_producto.py
"""

from __future__ import annotations

import base64
import binascii
import mimetypes
import os
import sys
from datetime import datetime
from pathlib import Path

# ----------------------------------------------------------------------------
# Configuración
# ----------------------------------------------------------------------------

REFERENCIA = Path("./referencia/reebok.jpeg")
SALIDAS = Path("./salidas")

GEMINI_MODEL = "gemini-3.1-flash-image-preview"   # Nano Banana 2
OPENAI_MODEL = "gpt-image-2"
OPENAI_SIZE = "1024x1536"                          # vertical
OPENAI_EDITS_URL = "https://api.openai.com/v1/images/edits"

PROMPT = (
    "Full-body photo of a young person walking through a gritty urban street in "
    "Buenos Aires, wearing this exact navy blue Reebok nylon tracksuit (zip jacket "
    "with grey side stripes, matching jogger pants with elastic cuffs). Keep the "
    "garment identical to the reference. Overcast natural light, slight 90s-2000s "
    "grain, shallow depth of field, confident stride, concrete walls and stencil "
    "graffiti in the background. Photorealistic, editorial street style."
)


# ----------------------------------------------------------------------------
# Utilidades
# ----------------------------------------------------------------------------

def log(msg: str) -> None:
    print(msg, flush=True)


def asegurar_carpetas() -> None:
    """Crea las carpetas de entrada/salida si no existen."""
    REFERENCIA.parent.mkdir(parents=True, exist_ok=True)
    SALIDAS.mkdir(parents=True, exist_ok=True)


def validar_referencia() -> bytes:
    """Devuelve los bytes de la imagen de referencia o aborta con mensaje claro."""
    if not REFERENCIA.exists():
        raise SystemExit(
            f"[ERROR] No se encontró la imagen de referencia en '{REFERENCIA}'.\n"
            f"        Colocá ahí la foto del conjunto Reebok y volvé a ejecutar."
        )
    data = REFERENCIA.read_bytes()
    if not data:
        raise SystemExit(f"[ERROR] La referencia '{REFERENCIA}' está vacía.")
    return data


def mime_de(path: Path) -> str:
    """Adivina el mime-type de la referencia (default image/jpeg)."""
    mime, _ = mimetypes.guess_type(str(path))
    return mime or "image/jpeg"


def nombre_salida(motor: str, ext: str = "png") -> Path:
    """Nombre único por motor + timestamp para no pisar salidas previas."""
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return SALIDAS / f"soul_manteca_{motor}_{ts}.{ext}"


def decodificar_b64(valor) -> bytes:
    """
    Decodifica de forma robusta lo que devuelven los motores.

    - Si ya son bytes binarios (p.ej. el SDK de Gemini suele entregar bytes ya
      decodificados), se devuelven tal cual.
    - Si es un str base64 (lo que devuelve OpenAI en b64_json, o algunas versiones
      del SDK), se decodifica.
    """
    if isinstance(valor, (bytes, bytearray)):
        # Heurística: ¿es base64 dentro de bytes ascii o ya es binario crudo?
        # Las firmas de PNG/JPEG empiezan con bytes no-ascii, así que si esto
        # arranca con un magic number conocido, ya es binario.
        if valor[:8].startswith(b"\x89PNG") or valor[:3] == b"\xff\xd8\xff":
            return bytes(valor)
        try:
            return base64.b64decode(valor, validate=True)
        except (binascii.Error, ValueError):
            return bytes(valor)
    if isinstance(valor, str):
        return base64.b64decode(valor)
    raise TypeError(f"Tipo de dato de imagen no soportado: {type(valor)!r}")


# ----------------------------------------------------------------------------
# Motor 1 — Google Gemini (google-genai)
# ----------------------------------------------------------------------------

def generar_gemini(img_bytes: bytes, mime: str) -> Path | None:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        log("[Gemini] Salteado: falta la variable de entorno GEMINI_API_KEY.")
        return None

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        log("[Gemini] Salteado: falta el SDK. Instalá con: pip install google-genai")
        return None

    log(f"[Gemini] Generando con modelo '{GEMINI_MODEL}' (imagen-a-imagen)...")
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=[
                types.Part.from_bytes(data=img_bytes, mime_type=mime),
                PROMPT,
            ],
        )
    except Exception as exc:  # noqa: BLE001 - queremos un mensaje legible
        log(f"[Gemini] ERROR de API: {type(exc).__name__}: {exc}")
        return None

    # Buscar la primera parte que contenga datos de imagen.
    candidates = getattr(response, "candidates", None) or []
    for cand in candidates:
        content = getattr(cand, "content", None)
        parts = getattr(content, "parts", None) or []
        for part in parts:
            inline = getattr(part, "inline_data", None)
            if inline and getattr(inline, "data", None):
                ext = (inline.mime_type or "image/png").split("/")[-1]
                destino = nombre_salida("gemini", ext)
                try:
                    destino.write_bytes(decodificar_b64(inline.data))
                except Exception as exc:  # noqa: BLE001
                    log(f"[Gemini] ERROR al decodificar/guardar: {exc}")
                    return None
                log(f"[Gemini] OK -> {destino}")
                return destino

    # Si llegamos acá, no vino imagen. Mostrar texto/razón si lo hay.
    texto = getattr(response, "text", None)
    log("[Gemini] La respuesta no contiene imagen.")
    if texto:
        log(f"[Gemini] Texto devuelto por el modelo: {texto.strip()[:500]}")
    return None


# ----------------------------------------------------------------------------
# Motor 2 — OpenAI (gpt-image-2 vía /v1/images/edits)
# ----------------------------------------------------------------------------

def generar_openai(ref_path: Path, mime: str) -> Path | None:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        log("[OpenAI] Salteado: falta la variable de entorno OPENAI_API_KEY.")
        return None

    try:
        import requests
    except ImportError:
        log("[OpenAI] Salteado: falta 'requests'. Instalá con: pip install requests")
        return None

    log(f"[OpenAI] Generando con modelo '{OPENAI_MODEL}' (/v1/images/edits)...")
    try:
        with ref_path.open("rb") as fh:
            files = {"image": (ref_path.name, fh, mime)}
            data = {
                "model": OPENAI_MODEL,
                "prompt": PROMPT,
                "size": OPENAI_SIZE,
                "n": "1",
            }
            resp = requests.post(
                OPENAI_EDITS_URL,
                headers={"Authorization": f"Bearer {api_key}"},
                files=files,
                data=data,
                timeout=300,
            )
    except requests.RequestException as exc:
        log(f"[OpenAI] ERROR de red: {exc}")
        return None

    # Manejo de errores HTTP con mensajes legibles.
    if resp.status_code != 200:
        detalle = _detalle_error_openai(resp)
        if _es_org_no_verificada(resp, detalle):
            log(
                "[OpenAI] Tu organización NO está verificada para usar "
                f"'{OPENAI_MODEL}'.\n"
                "         Verificala en: https://platform.openai.com/settings/organization/general\n"
                "         (puede tardar hasta ~15 min en activarse tras verificar).\n"
                f"         Detalle de la API: {detalle}"
            )
        else:
            log(f"[OpenAI] ERROR HTTP {resp.status_code}: {detalle}")
        return None

    try:
        payload = resp.json()
        b64 = payload["data"][0]["b64_json"]
    except (ValueError, KeyError, IndexError) as exc:
        log(f"[OpenAI] Respuesta inesperada de la API: {exc}\n{resp.text[:500]}")
        return None

    destino = nombre_salida("openai", "png")
    try:
        destino.write_bytes(decodificar_b64(b64))
    except Exception as exc:  # noqa: BLE001
        log(f"[OpenAI] ERROR al decodificar/guardar: {exc}")
        return None

    log(f"[OpenAI] OK -> {destino}")
    return destino


def _detalle_error_openai(resp) -> str:
    """Extrae un mensaje de error legible del cuerpo de la respuesta."""
    try:
        j = resp.json()
        err = j.get("error", {})
        return err.get("message") or str(j)
    except ValueError:
        return resp.text[:500]


def _es_org_no_verificada(resp, detalle: str) -> bool:
    """Detecta el caso típico de organización sin verificar."""
    texto = (detalle or "").lower()
    señales = ("must be verified", "organization", "verify", "verified")
    return resp.status_code == 403 and any(s in texto for s in señales)


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main() -> int:
    log("== Soul Manteca · generador de imágenes de producto ==")
    asegurar_carpetas()
    img_bytes = validar_referencia()
    mime = mime_de(REFERENCIA)
    log(f"Referencia: {REFERENCIA} ({len(img_bytes)} bytes, {mime})")

    resultados = []
    resultados.append(("Gemini", generar_gemini(img_bytes, mime)))
    resultados.append(("OpenAI", generar_openai(REFERENCIA, mime)))

    log("\n== Resumen ==")
    ok = 0
    for motor, destino in resultados:
        if destino:
            ok += 1
            log(f"  ✓ {motor}: {destino}")
        else:
            log(f"  ✗ {motor}: sin salida (ver mensajes arriba)")

    # Código de salida: 0 si al menos un motor generó imagen, 1 si ninguno.
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
