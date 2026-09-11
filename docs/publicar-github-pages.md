---
proyecto: Panel de Seguimiento Inspirare
tipo: instructivo
estado: vigente
fecha: 2026-09-11
---

# Cómo publicar el sitio en GitHub Pages

El código ya está en GitHub (`fperulan/panel_inspirare`, repo privado) y el
workflow que hace la publicación ([.github/workflows/deploy.yml](../.github/workflows/deploy.yml))
ya está commiteado. Faltan dos configuraciones que sólo se hacen **una vez**,
directamente en la web de GitHub — no hace falta terminal.

## 1. Cargar el secret con las credenciales de login

El sitio pide usuario y contraseña (ver
[`decisiones/002-login-y-control-de-acceso.md`](decisiones/002-login-y-control-de-acceso.md)).
Esas credenciales viven en un secret de GitHub, nunca en el código.

1. Entrar a `https://github.com/fperulan/panel_inspirare/settings/secrets/actions`
   (o: repo → **Settings** → en el menú de la izquierda, **Secrets and
   variables** → **Actions**).
2. Botón **New repository secret**.
3. **Name**: `PANEL_USERS`
4. **Secret**: por ahora, una sola cuenta simple para validar —
   ```json
   [{"usuario": "admin", "nombre": "Admin", "password": "12345"}]
   ```
   (cambiá `12345` por lo que prefieras; cuando se sume el resto del equipo,
   se agregan más objetos a esta misma lista).
5. **Add secret**.

## 2. Habilitar Pages con GitHub Actions como origen

1. Repo → **Settings** → **Pages** (menú de la izquierda).
2. En **Build and deployment → Source**, elegir **GitHub Actions** (no
   "Deploy from a branch").
3. No hace falta guardar nada más — al elegir la opción ya queda configurado.

## 3. Disparar la primera publicación

El workflow corre solo en cada push a `main` que toque `sitio/`, pero como
recién se habilitó Pages, conviene dispararlo a mano una vez:

1. Repo → pestaña **Actions**.
2. En la lista de la izquierda, click en **Publicar sitio**.
3. Botón **Run workflow** (arriba a la derecha) → **Run workflow** de nuevo
   para confirmar.
4. Esperar a que el run termine con el ✓ verde (tarda menos de un minuto).

## 4. Ver el sitio publicado

- Repo → **Settings** → **Pages** va a mostrar la URL pública, algo como
  `https://fperulan.github.io/panel_inspirare/`.
- También aparece como link en el propio run del workflow (pestaña Actions →
  el run → job **deploy** → link "github-pages").

Entrar con `admin` / la contraseña que hayas puesto en el secret.

## Nota sobre privacidad

El repo es privado, pero **la URL de GitHub Pages es pública** — cualquiera
que la tenga puede abrirla (el login sólo identifica, no bloquea el acceso a
los archivos; ver la ADR 002). No compartir el link fuera del equipo.

## Actualizar credenciales más adelante

Editar el secret `PANEL_USERS` (mismo lugar del paso 1) con la lista
completa de personas, y volver a correr el workflow (paso 3) para que tome
el cambio — un push normal a `sitio/` también lo dispara solo.
