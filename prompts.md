# Soul Manteca — Prompts de generación (foto y video)

Banco de prompts para generar contenido de producto con IA (imagen-a-imagen),
manteniendo la prenda idéntica a la referencia y recreando distintos contextos.

---

## 🧩 Cómo cargar las imágenes (roles por orden)

Los modelos no adivinan para qué es cada imagen: hay que asignarle un rol a cada
una **por su orden** y nombrarlas en el texto. Subí siempre en este orden:

| Imagen | Rol |
|--------|-----|
| **Imagen 1** | La prenda (producto). Se mantiene idéntica. |
| **Imagen 2** | El contexto / escenario / estilo. Solo ambiente, NO la cara. |
| **Imagen 3** | El logo (opcional). Referencia exacta del logo Reebok. |

- En Flow (video): modo **Ingredients** → cargás cada imagen como ingrediente.
- En Nano Banana / Gemini y OpenAI /images/edits: se pasan varias imágenes seguidas.
- Regla de oro: decí **qué tomar de cada imagen** y **qué NO copiar** (la cara, la persona).

---

## 👕 Descripción del conjunto Reebok (para el hueco `[PRENDA]` / `[GARMENT]`)

**🇪🇸**
> Conjunto deportivo Reebok vintage de nylon azul marino. La CAMPERA: con cierre
> completo, vivos/líneas grises a los costados y en las mangas, cuello interior gris,
> y el logo Reebok (con el isotipo vectorial y la palabra "Reebok") en el pecho. El
> PANTALÓN: jogger azul marino liso a juego, con puños elásticos, SIN líneas grises
> (las líneas grises están ÚNICAMENTE en la campera); lleva solo el mismo logo Reebok
> pequeño cerca del tobillo. Mantené el color azul marino, el corte de nylon y el logo
> exactamente iguales a la referencia.

**🇬🇧**
> Vintage navy blue Reebok nylon tracksuit. The JACKET: full zip, grey side
> stripes/piping along the sides and sleeves, grey inner collar, and the Reebok logo
> (vector symbol + "Reebok" wordmark) on the chest. The PANTS: plain matching navy
> joggers with elastic cuffs, NO grey stripes (the grey lines are ONLY on the jacket);
> they carry only the same small Reebok logo near the ankle. Keep the navy color, the
> nylon cut and the logo exactly identical to the reference.

### Línea del logo (si agregás imagen 3)
**🇪🇸** Usá la imagen 3 SOLO como referencia exacta del logo Reebok — reproducí ese
logo de forma fiel en el pecho y el tobillo. No inventes ni modifiques el logo.

**🇬🇧** Use image 3 ONLY as the exact Reebok logo reference — reproduce this logo
faithfully on the chest and ankle. Do not invent or alter the logo.

> ⚠️ Los modelos suelen deformar texto/logos chicos (sobre todo en video). La imagen 3
> ayuda mucho, pero si sale mal, reforzá/corregí el logo después en edición.

---

## 📸 PROMPT MAESTRO (foto, estética bodega candid)

**🇪🇸**
> Foto candid documental fotorrealista, en film de 35mm, estética vintage Y2K.
> USÁ LAS IMÁGENES ASÍ: Imagen 1 = la prenda → [PRENDA]; mantenela 100% idéntica.
> Imagen 2 = contexto y clima → recreá el mismo ambiente, luz, paleta y energía
> espontánea, solo como estilo/locación, NO para la identidad de la persona.
> Imagen 3 = logo → reproducí el logo Reebok de forma fiel.
> NO copies ninguna cara: la cara del modelo debe estar oculta, fuera de cuadro o
> girada. Momento natural y sin pose, encuadre apenas descentrado tipo foto de un amigo.
> Look: grano de película, mezcla de luz fluorescente cálida y natural, colores
> nostálgicos algo saturados, textura auténtica de piel y tela, sin aspecto plástico.
> Fotorrealista, sin textos ni marcas de agua.

**🇬🇧**
> Photorealistic candid documentary photo, shot on 35mm film, vintage Y2K aesthetic.
> USE THE IMAGES AS FOLLOWS: Image 1 = the garment → [GARMENT]; keep it 100% identical.
> Image 2 = context and mood → recreate the same environment, lighting, color grade and
> candid energy, as style/setting only, NOT for the person's identity. Image 3 = logo →
> reproduce the Reebok logo faithfully. DO NOT copy any face: the model's face must be
> hidden, cropped out of frame, or turned away. Natural unposed moment, slightly
> off-center snapshot framing. Look: film grain, warm fluorescent + natural light mix,
> slightly saturated nostalgic colors, authentic skin and fabric texture, no plastic CGI
> look. Photorealistic, no text overlays, no watermarks.

---

# 🎬 PROMPTS DE VIDEO POR CONTEXTO (10s, Flow / Veo)

Convención: **Imagen 1 = prenda, Imagen 2 = contexto, Imagen 3 = logo.**
Por defecto `[PRENDA]` / `[GARMENT]` = la descripción del Reebok de arriba.

---

## 1 — Supermercado fisheye

**🇪🇸**
> Video fotorrealista de 10 segundos, estética vintage Y2K, lente ojo de pez con fuerte
> distorsión. Imagen 1 = la prenda: [PRENDA] (mantenela idéntica). Imagen 2 = contexto:
> interior de supermercado, pasillo largo con estanterías curvadas repletas de productos
> coloridos, luz fluorescente, piso de baldosas. Imagen 3 = logo Reebok exacto. No copies
> ninguna cara. Tomas (10s): (1) POV cenital desde un carrito que avanza por el pasillo,
> piernas y zapatillas al frente; (2) la cámara fisheye gira y las góndolas se curvan;
> (3) cierre sobre el detalle de la prenda. Movimiento hacia adelante constante. Look:
> grano de película, colores saturados, luz fluorescente cálida, leve cámara en mano.
> Foco en el outfit, caras fuera de cuadro. Audio: ambiente de súper, ruedas del carrito,
> murmullo lejano, sin música.

**🇬🇧**
> 10-second photorealistic video, vintage Y2K aesthetic, fisheye lens with heavy
> distortion. Image 1 = the garment: [GARMENT] (keep it identical). Image 2 = context:
> supermarket interior, long aisle with curved shelves packed with colorful products,
> fluorescent light, tiled floor. Image 3 = exact Reebok logo. Do NOT copy any face.
> Shots (10s): (1) overhead POV from a moving shopping cart gliding down the aisle, the
> model's legs and sneakers in front; (2) the fisheye camera tilts, shelves curving around
> the frame; (3) close-up on the garment detail. Constant forward motion. Look: film grain,
> saturated colors, warm fluorescent light, subtle handheld feel. Focus on the outfit,
> faces out of frame. Audio: supermarket ambience, cart wheels, distant chatter, no music.

---

## 2 — Caminata street-style NYC (día, vereda)

**🇪🇸**
> Video fotorrealista de 10 segundos, street-style candid tipo paparazzi, luz de día.
> Imagen 1 = la prenda: [PRENDA] (idéntica). Imagen 2 = contexto: vereda de Nueva York,
> edificios de ladrillo, baranda de un café con plantas y flores, transeúntes desenfocados.
> Imagen 3 = logo Reebok exacto. No copies caras. Tomas (10s): (1) plano entero caminando
> hacia la cámara con paso seguro y relajado; (2) la cámara retrocede acompañando el andar;
> (3) leve contrapicado que resalta el calce del pantalón y las zapatillas. Look: luz
> natural suave, leve grano, poca profundidad de campo, paleta realista. El protagonista es
> el outfit; la cara fuera de cuadro o girada. Audio: ambiente urbano, pasos, tráfico
> lejano, sin música.

**🇬🇧**
> 10-second photorealistic video, candid paparazzi street-style, daylight. Image 1 = the
> garment: [GARMENT] (identical). Image 2 = context: New York sidewalk, brick buildings, a
> café railing with plants and flowers, blurred passersby. Image 3 = exact Reebok logo. Do
> NOT copy faces. Shots (10s): (1) full-body shot walking toward the camera with a
> confident, relaxed stride; (2) the camera tracks backward following the walk; (3) slight
> low angle highlighting the trouser fit and sneakers. Look: soft natural light, slight
> grain, shallow depth of field, realistic palette. The outfit is the hero; face out of
> frame or turned away. Audio: urban ambience, footsteps, distant traffic, no music.

---

## 3 — Plaza brutalista (vista de espalda, brazos abiertos)

**🇪🇸**
> Video fotorrealista de 10 segundos, estética urbana cruda. Imagen 1 = la prenda:
> [PRENDA] (idéntica en color, corte, vivos grises de la campera y logo). Imagen 2 =
> contexto: explanada urbana tipo Av. Paulista, gran edificio brutalista de vidrio al
> fondo, maceteros de cemento con graffiti, cielo nublado. Imagen 3 = logo Reebok exacto.
> No copies caras. Tomas (10s): (1) plano entero del modelo de espaldas, abriendo lentamente
> los brazos en cruz para mostrar el diseño y el logo; (2) dolly-in lento hacia el pecho/logo
> al girar levemente; (3) leve órbita lateral. Movimiento pausado y cinematográfico. Look:
> luz nublada plana, leve grano, colores apagados, sensación de registro real. Foco total en
> la prenda; nunca se ve la cara (de espaldas). Audio: viento suave, ambiente de plaza
> lejano, sin música.

**🇬🇧**
> 10-second photorealistic video, raw urban aesthetic. Image 1 = the garment: [GARMENT]
> (identical in color, cut, the jacket's grey stripes and logo). Image 2 = context: an open
> urban plaza like Avenida Paulista, a large brutalist glass tower in the background,
> concrete planters with graffiti, overcast sky. Image 3 = exact Reebok logo. Do NOT copy
> faces. Shots (10s): (1) full-body shot from behind, slowly spreading arms wide to reveal
> the design and logo; (2) a slow dolly-in toward the chest/logo as the model turns slightly;
> (3) a slight lateral orbit. Slow, cinematic movement. Look: flat overcast light, slight
> grain, muted colors, real-footage feel. Total focus on the garment; the face is never seen
> (faces away). Audio: soft wind, distant plaza ambience, no music.

---

## 4 — Caminata invernal NYC (varias personas / varias prendas)

**🇪🇸**
> Video fotorrealista de 10 segundos, street-style candid, día nublado. Imagen 1 = prendas:
> podés vestir DOS modelos → modelo A con [PRENDA] (el Reebok) y modelo B con [PRENDA 2:
> describir otra prenda]. Mantené ambas idénticas. Imagen 2 = contexto: calle de Nueva York,
> veredas anchas, edificios, gente desenfocada de fondo. Imagen 3 = logo Reebok exacto. No
> copies caras. Tomas (10s): (1) los dos modelos caminando juntos hacia la cámara, uno con
> café en mano; (2) la cámara retrocede mostrando ambos outfits de cuerpo entero; (3) cierre
> sobre los detalles de las dos prendas. Caminar natural y relajado. Look: luz fría difusa,
> leve grano, paleta de invierno realista. Foco en los dos outfits, no las caras. Audio:
> ambiente de ciudad, pasos, conversación ininteligible, sin música.

**🇬🇧**
> 10-second photorealistic video, candid street-style, overcast day. Image 1 = garments:
> you may dress TWO models → model A in [GARMENT] (the Reebok) and model B in [GARMENT 2:
> describe another item]. Keep both identical. Image 2 = context: a New York street, wide
> sidewalks, buildings, blurred people in the background. Image 3 = exact Reebok logo. Do
> NOT copy faces. Shots (10s): (1) the two models walking together toward the camera, one
> holding a coffee cup; (2) the camera tracks backward showing both full-body outfits; (3)
> close-up on the details of the two garments. Natural, relaxed walk. Look: cold diffused
> light, slight grain, realistic winter palette. Focus on the two outfits, not the faces.
> Audio: city ambience, footsteps, unintelligible background conversation, no music.

---

## 5 — Crew junto a la pared de ladrillo (UK, varias prendas)

**🇪🇸**
> Video fotorrealista de 10 segundos, estética cruda documental tipo grime UK de los 2000s,
> día gris. Imagen 1 = prendas: podés vestir TRES modelos → modelo A con [PRENDA] (el Reebok),
> modelo B con [PRENDA 2] y modelo C con [PRENDA 3] (conjuntos/camperas oversize). Mantené
> cada prenda idéntica. Imagen 2 = contexto: pared de ladrillo a la calle, vereda, mochilas en
> el piso, luz nublada de Londres. Imagen 3 = logo Reebok exacto. No copies caras (capuchas,
> gorros o encuadre las dejan fuera). Tomas (10s): (1) plano del grupo parado contra la pared,
> lenguaje corporal relajado; (2) paneo lento que recorre los tres outfits de arriba abajo;
> (3) cierre sobre el detalle de una prenda. Movimiento sutil, casi estático. Look: luz plana
> nublada, grano marcado, colores apagados, sensación de foto de archivo real. Foco absoluto
> en la ropa; las caras no se ven. Audio: viento, ambiente de calle, voces lejanas, sin música.

**🇬🇧**
> 10-second photorealistic video, raw documentary aesthetic like early-2000s UK grime, grey
> day. Image 1 = garments: you may dress THREE models → model A in [GARMENT] (the Reebok),
> model B in [GARMENT 2] and model C in [GARMENT 3] (tracksuits / oversized jackets). Keep
> each garment identical. Image 2 = context: a roadside brick wall, sidewalk, bags on the
> ground, overcast London light. Image 3 = exact Reebok logo. Do NOT copy faces (hoods,
> beanies or framing keep them out). Shots (10s): (1) shot of the group standing against the
> wall, relaxed body language; (2) a slow pan traveling over the three outfits top to bottom;
> (3) close-up on one garment's detail. Subtle, almost static movement. Look: flat overcast
> light, heavy grain, muted colors, archival real-photo feel. Absolute focus on the clothing;
> faces are not seen. Audio: wind, street ambience, distant voices, no music.

---

## 💡 Reglas de oro

1. **Orden = rol:** subí las imágenes en el orden que las nombrás (1 prenda, 2 contexto, 3 logo).
2. **Decí qué tomar de cada imagen** y **qué NO copiar** (la cara, la persona).
3. **Repetí "mantené la prenda idéntica a la imagen 1"** — es lo que más se desvía.
4. **Una sola acción por clip** de 10s (caminar O abrir brazos O paneo).
5. En escenas con varias personas, **numerá las prendas** ([PRENDA 2], [PRENDA 3]…).
6. Veo suele respetar mejor el **inglés**; si el español falla, usá la versión EN.
