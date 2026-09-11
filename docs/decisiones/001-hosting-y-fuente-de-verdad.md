# 001 — Hosting y fuente de verdad

**Estado**: aceptada — 2026-09-11

## Contexto

Hay que elegir dónde vive el sitio y dónde vive la fuente de verdad de los
datos que muestra.

## Decisión

- **Hosting**: GitHub Actions + GitHub Pages. El repo ya da build, hosting,
  historial y permisos — no hace falta Vercel ni ninguna plataforma adicional.
- **Fuente de verdad**: los archivos Markdown en OneDrive, tal como el equipo
  ya los genera trabajando con Claude. El sitio lee; no edita (con la
  excepción controlada de los lineamientos, ver sección 7 de
  `00_Panel_Seguimiento.md`).

## Alternativas descartadas

- **Repo git como fuente de verdad, en lugar de OneDrive**: es lo más robusto
  y da historial real, pero obliga a Guido y Agustín a convivir con git.
  Queda como destino natural si el equipo se adapta más adelante — no se
  descarta para siempre, se pospone.
- **Edición desde la web**: generaría dos fuentes de verdad (los Markdown y lo
  editado en el sitio) y pudre el sistema. Ver principio de diseño 4 en
  `00_Panel_Seguimiento.md`.

## Consecuencias

El recolector (Etapa 2) depende de Microsoft Graph API para leer OneDrive, en
lugar de un simple `git pull`. Es más trabajo de integración a cambio de no
imponerle git a todo el equipo.
