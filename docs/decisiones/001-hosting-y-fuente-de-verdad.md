# 001 — Hosting y fuente de verdad

**Estado**: aceptada, hosting revisado — 2026-09-11 (actualizada 2026-09-11)

## Contexto

Hay que elegir dónde vive el sitio y dónde vive la fuente de verdad de los
datos que muestra.

## Decisión

- **Hosting**: **Azure Static Web Apps** (capa gratuita). Revisado el mismo
  día en que se aceptó — ver "Revisión" más abajo.
- **Fuente de verdad**: los archivos Markdown en OneDrive, tal como el equipo
  ya los genera trabajando con Claude. El sitio lee; no edita (con la
  excepción controlada de los lineamientos, ver sección 7 de
  `00_Panel_Seguimiento.md`).

## Revisión 2026-09-11 — de GitHub Pages a Azure Static Web Apps

La decisión original era GitHub Actions + GitHub Pages. Se cayó en cuanto se
intentó usar: **GitHub Pages no está disponible con repositorio privado en el
plan gratis de GitHub** (pide pasar el repo a público o pagar GitHub Pro). El
repo se había puesto en privado ese mismo día por los datos reales de cliente
que contiene el propio sitio y la documentación — volver a público no era
aceptable.

Se evaluaron tres salidas: volver el repo a público, pagar GitHub Pro, o
migrar de hosting. Se eligió migrar a **Azure Static Web Apps**: capa
gratuita, se despliega desde el repo privado sin exponerlo (usa un token de
deploy, no requiere que el repo sea público), y además deja preparado el
camino para el control de acceso real con Entra ID que quedó pendiente en la
ADR 002 — sin implementarlo todavía, sólo sin tener que migrar de nuevo el
día que haga falta.

## Alternativas descartadas

- **GitHub Pages**: descartada por la limitación de plan gratis + repo
  privado explicada arriba.
- **Pagar GitHub Pro**: mantenía todo igual, pero suma un costo recurrente
  sólo para esto.
- **Cloudflare Pages / Netlify**: también gratis y compatibles con repos
  privados, pero alejan la infraestructura del ecosistema Microsoft que ya
  se usa para todo lo demás (OneDrive, Teams, Power BI, y Azure para el
  recolector de la Etapa 2).
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
