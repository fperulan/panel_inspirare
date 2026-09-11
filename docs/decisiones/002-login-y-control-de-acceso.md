# 002 — Login y control de acceso

**Estado**: aceptada (versión simple) — 2026-09-11

## Contexto

Se pidió que el sitio identifique quién lo está mirando y le muestre en un
perfil sus propios movimientos recientes (filtrando la bitácora por autor).

Se evaluaron dos rutas:

- **Microsoft Entra ID** (MSAL.js, client-side): reutiliza las cuentas
  Microsoft 365 que ya tiene todo el equipo, sin mantener contraseñas
  propias. Requiere permisos de administrador en el tenant de Inspirare para
  crear el app registration.
- **Login propio, simple**: usuario/contraseña validados en el navegador
  contra hashes generados a partir de un secret de GitHub. No depende de
  permisos de Entra ID.

**Decisión (2026-09-11)**: por ahora, **login propio y simple** — no hace
falta Entra ID para esta etapa. Se puede reabrir esta ADR más adelante si
hace falta algo más robusto.

## Cómo funciona

1. Los usuarios y contraseñas en texto plano viven en **un solo secret de
   GitHub** (`PANEL_USERS`, JSON: `[{"usuario","nombre","password"}, ...]`),
   configurado en Settings → Secrets and variables → Actions. Nunca se
   commitean.
2. El workflow de publicación (`.github/workflows/deploy.yml`) corre
   `scripts/build_usuarios.py`, que lee ese secret y escribe
   `sitio/usuarios.json` con el hash SHA-256 de cada contraseña — nunca la
   contraseña en texto plano.
3. En el navegador, `sitio/index.html` pide usuario y contraseña, hashea la
   contraseña con `crypto.subtle` (Web Crypto, sin librerías) y la compara
   contra `usuarios.json`. Si coincide, guarda `{usuario, nombre}` en
   `sessionStorage` — dura lo que dura la pestaña.
4. La vista "Mi perfil" filtra la bitácora de todos los proyectos por
   `autor === nombre` de la sesión activa.

## Limitación conocida — aceptada a propósito

Esto es identificación, **no es control de acceso real**. GitHub Pages sirve
los archivos estáticos (incluido `usuarios.json` y `state.json`) a cualquiera
que tenga el link directo, esté logueado o no — el login sólo decide qué
*muestra la pantalla*. Es suficiente para saber quién es cada persona del
equipo y armarle un perfil; no alcanza si en algún momento hace falta que
alguien sin cuenta no pueda ver los datos en absoluto. Si eso pasa a
importar, la alternativa sigue siendo migrar a Azure Static Web Apps (o
volver a evaluar Entra ID) — no se descarta, sólo se pospone.

## Pendiente

- Cargar el secret `PANEL_USERS` en GitHub con las personas reales del
  equipo (Fernando, Agustín, Guido, JMD).
- Habilitar Pages con source "GitHub Actions" en la configuración del repo.
- El campo `nombre` de cada usuario debe coincidir exactamente con el
  `autor` usado en las bitácoras para que "Mi perfil" encuentre sus
  registros — hoy es texto libre (ej. "JMD" vs "Juan Manuel Daher"), así que
  conviene fijar un nombre corto único por persona y usarlo siempre igual en
  ambos lugares.
