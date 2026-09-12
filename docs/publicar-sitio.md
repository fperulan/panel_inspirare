---
proyecto: Panel de Seguimiento Inspirare
tipo: instructivo
estado: vigente
fecha: 2026-09-11
---

# Cómo publicar el sitio (GitHub Pages)

El código ya está en GitHub (`fperulan/panel_inspirare`) y el workflow que
hace la publicación ([.github/workflows/deploy.yml](../.github/workflows/deploy.yml))
ya está commiteado. Faltan dos configuraciones que sólo se hacen **una vez**.

> **Nota**: el mismo día se probó Azure Static Web Apps y se volvió atrás
> porque pedía cargar una tarjeta para cualquier suscripción de Azure, incluso
> para el plan gratis. Se decidió, por ahora, pasar el repo a **público** para
> poder usar GitHub Pages sin esa fricción y validar rápido. Historial
> completo, con los trade-offs de cada camino, en
> [`decisiones/001-hosting-y-fuente-de-verdad.md`](decisiones/001-hosting-y-fuente-de-verdad.md).

## 0. Repo público

GitHub Pages no funciona con repo privado en el plan gratis de GitHub.
Settings → General → Danger Zone → **Change visibility** → **Make public**.

## 1. Cargar el secret con las credenciales de login

El sitio pide usuario y contraseña (ver
[`decisiones/002-login-y-control-de-acceso.md`](decisiones/002-login-y-control-de-acceso.md)).

1. Entrar a `https://github.com/fperulan/panel_inspirare/settings/secrets/actions`.
2. **New repository secret** → **Name**: `PANEL_USERS` → **Secret**:
   ```json
   [{"usuario": "admin", "nombre": "Admin", "password": "12345"}]
   ```
3. **Add secret**.

## 2. Habilitar Pages con GitHub Actions como origen

1. Repo → **Settings** → **Pages**.
2. **Build and deployment → Source**: elegir **GitHub Actions**.

## 3. Disparar la primera publicación

1. Repo → pestaña **Actions** → workflow **Publicar sitio**.
2. **Run workflow** → **Run workflow** para confirmar.
3. Esperar el ✓ verde.

## 4. Ver el sitio publicado

Settings → Pages muestra la URL (algo como
`https://fperulan.github.io/panel_inspirare/`). Entrar con `admin` / la
contraseña del secret.

## Nota sobre privacidad

El repo ahora es público — cualquiera puede ver el código y la
documentación, incluidos nombres reales y contexto comercial de LP SA en
`sitio/index.html` y en `docs/*.md`. `Modelo de proyecto real/` sigue
excluido por `.gitignore` y no se sube. Esta es una decisión consciente para
validar rápido (2026-09-11) — si más adelante hace falta volver a privado,
el camino ya explorado es Azure Static Web Apps (ver ADR 001), resolviendo
antes el tema de la tarjeta.

## Actualizar credenciales más adelante

Editar el secret `PANEL_USERS` (paso 1) y volver a correr el workflow (paso
3) — un push normal a `sitio/` también lo dispara solo.
