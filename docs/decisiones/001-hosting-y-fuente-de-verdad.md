# 001 — Hosting y fuente de verdad

**Estado**: aceptada, hosting revisado dos veces en el mismo día — 2026-09-11

## Contexto

Hay que elegir dónde vive el sitio y dónde vive la fuente de verdad de los
datos que muestra.

## Decisión (vigente)

- **Hosting**: **GitHub Pages**, con el **repo público**. Ver "Revisión 2"
  más abajo para el porqué de volver acá después de probar Azure.
- **Fuente de verdad**: los archivos Markdown en OneDrive, tal como el equipo
  ya los genera trabajando con Claude. El sitio lee; no edita (con la
  excepción controlada de los lineamientos, ver sección 7 de
  `00_Panel_Seguimiento.md`).

## Revisión 1 (2026-09-11) — de GitHub Pages a Azure Static Web Apps

La decisión original era GitHub Actions + GitHub Pages con **repo privado**.
Se cayó en cuanto se intentó usar: **GitHub Pages no está disponible con
repositorio privado en el plan gratis de GitHub** (pide pasar el repo a
público o pagar GitHub Pro). El repo se había puesto en privado ese mismo día
por los datos reales de cliente que contiene el propio sitio y la
documentación — volver a público no parecía aceptable en ese momento.

Se migró a **Azure Static Web Apps**: capa gratuita, se despliega desde el
repo privado sin exponerlo, y de paso deja preparado el camino para el
control de acceso real con Entra ID (ADR 002).

## Revisión 2 (2026-09-11, mismo día) — vuelta a GitHub Pages, repo público

Al crear el recurso en Azure apareció otra fricción: **Azure exige una
suscripción con tarjeta cargada para cualquier recurso, incluso el plan
gratis** (a diferencia de GitHub Pages, Cloudflare Pages o Netlify, que no
piden tarjeta). El tenant de Inspirare en Azure no tenía ninguna suscripción
activa, y activar una implicaba resolver primero de quién es la tarjeta —
algo que no se quería frenar a esperar.

**Decisión**: pasar el repo a **público** y volver a **GitHub Pages** para
validar rápido, aceptando conscientemente que el código y la documentación
quedan visibles (`Modelo de proyecto real/` sigue afuera por `.gitignore`,
pero `sitio/index.html` y los `docs/*.md` sí tienen nombres reales y contexto
comercial de LP SA). Si más adelante se resuelve el tema de la tarjeta,
volver a Azure Static Web Apps con repo privado sigue siendo el camino ya
explorado — el workflow y la documentación de esa opción quedaron descritos
acá arriba, por si hace falta retomarlos.

## Alternativas descartadas

- **Pagar GitHub Pro**: mantenía el repo privado, pero suma un costo
  recurrente sólo para esto.
- **Cloudflare Pages / Netlify**: gratis de verdad, sin pedir tarjeta, y
  compatibles con repos privados — hubieran evitado las dos fricciones
  anteriores. Se descartaron por alejarse del ecosistema Microsoft que ya se
  usa para todo lo demás, pero quedan como opción de respaldo si GitHub
  Pages da algún problema.
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
