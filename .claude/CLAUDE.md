# Panel de Seguimiento Inspirare — instrucciones de repo

Contexto completo en [`docs/00_Panel_Seguimiento.md`](../docs/00_Panel_Seguimiento.md).
Antes de proponer cambios de arquitectura, leerlo entero — ya resuelve varias
preguntas obvias (por qué no Planner/Loop, por qué OneDrive y no git, por qué
Azure Static Web Apps y no GitHub Pages).

## Reglas del proyecto

- **El sitio lee, no escribe.** Toda edición de datos vive en los Markdown de
  OneDrive. La única excepción es el flujo de lineamientos (append-only),
  descrito en la sección 7 del documento de traspaso.
- **`sitio/state.json` es generado.** No editarlo a mano una vez que exista;
  lo produce `recolector/build_state.py`.
- **No adelantar etapas del roadmap.** El roadmap (sección 9 del documento de
  traspaso) es secuencial a propósito — la Etapa 1 (contrato de datos)
  desbloquea todo lo demás. No tiene sentido escribir el recolector (Etapa 2)
  contra un contrato de datos que todavía no se aplicó a ningún proyecto real.
- **`Modelo de proyecto real/`** es una copia de referencia del proyecto
  Krikos (LP SA), para probar el parser sin depender de Microsoft Graph API.
  No es el proyecto real — no editar ahí pensando que se sincroniza a algún
  lado.

## Stack

Sitio estático sin build (`sitio/index.html`, HTML/CSS/JS plano). El
recolector y el correo semanal son Python. No introducir un framework de
frontend ni un bundler salvo que el documento de traspaso se actualice para
justificarlo — es una decisión de diseño, no un olvido.
