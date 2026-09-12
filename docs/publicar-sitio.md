---
proyecto: Panel de Seguimiento Inspirare
tipo: instructivo
estado: vigente
fecha: 2026-09-11
---

# Cómo publicar el sitio (Azure Static Web Apps)

El código ya está en GitHub (`fperulan/panel_inspirare`, repo privado) y el
workflow que hace la publicación ([.github/workflows/deploy.yml](../.github/workflows/deploy.yml))
ya está commiteado. Se cambió de GitHub Pages a **Azure Static Web Apps**
porque Pages no funciona con repo privado en el plan gratis de GitHub (ver
[`decisiones/001-hosting-y-fuente-de-verdad.md`](decisiones/001-hosting-y-fuente-de-verdad.md)).
Faltan tres configuraciones que sólo se hacen **una vez**.

## 1. Crear el recurso en Azure

1. Entrar a [portal.azure.com](https://portal.azure.com) → buscar **Static
   Web Apps** → **Create**.
2. **Resource group**: crear uno nuevo (ej. `panel-inspirare-rg`).
3. **Name**: `panel-inspirare` (o el que prefieras).
4. **Plan type**: **Free**.
5. **Región**: cualquiera cercana disponible para Static Web Apps (ej. East
   US 2, West Europe).
6. **Deployment details → Source**: elegir **Other** (no "GitHub") — así
   Azure no pide conectarse directo al repo, sólo crea el recurso y un token
   que se carga a mano en el paso 3. Es más simple que autorizar la app de
   GitHub de Azure.
7. **Review + create** → **Create**. Tarda menos de un minuto.

## 2. Copiar el token de deploy

1. Ir al recurso recién creado → **Overview**.
2. Botón **Manage deployment token** → copiar el valor.

## 3. Cargar los secrets en GitHub

En `https://github.com/fperulan/panel_inspirare/settings/secrets/actions`
(o: repo → **Settings** → **Secrets and variables** → **Actions**), crear
**dos** repository secrets:

- **`AZURE_STATIC_WEB_APPS_API_TOKEN`**: el token copiado en el paso 2.
- **`PANEL_USERS`**: las credenciales de login (ver
  [`decisiones/002-login-y-control-de-acceso.md`](decisiones/002-login-y-control-de-acceso.md)),
  por ejemplo:
  ```json
  [{"usuario": "admin", "nombre": "Admin", "password": "12345"}]
  ```

## 4. Disparar la publicación

1. Repo → pestaña **Actions** → workflow **Publicar sitio**.
2. **Run workflow** → **Run workflow** para confirmar.
3. Esperar el ✓ verde (menos de un minuto).

## 5. Ver el sitio publicado

La URL pública aparece en el recurso de Azure → **Overview** (algo como
`https://<nombre-random>.azurestaticapps.net`). Entrar con el usuario y
contraseña que hayas puesto en `PANEL_USERS`.

## Nota sobre privacidad

El repo es privado, pero **la URL del sitio publicado es pública** —
cualquiera que la tenga puede abrirla (el login sólo identifica, no bloquea
el acceso a los archivos; ver la ADR 002). No compartir el link fuera del
equipo. Azure Static Web Apps sí permite, más adelante, exigir login real
por ruta (`staticwebapp.config.json` + un proveedor de identidad como Entra
ID) si en algún momento hace falta bloquear el acceso de verdad — no está
configurado todavía, a propósito.

## Actualizar credenciales más adelante

Editar el secret `PANEL_USERS` (mismo lugar del paso 3) con la lista
completa de personas, y volver a correr el workflow (paso 4) para que tome
el cambio — un push normal a `sitio/` también lo dispara solo.
