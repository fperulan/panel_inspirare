---
proyecto: Panel de Seguimiento Inspirare
estado: prototipo
responsable: Fernando Perulan
fecha_documento: 2026-09-11
---

# Panel de Seguimiento — Inspirare Consulting

Documento de traspaso. Resume el problema, las decisiones tomadas y el plan de
construcción de una herramienta que lee el estado de los proyectos desde los
archivos Markdown que el equipo ya genera trabajando con Claude.

---

## 1. El problema

El equipo ya intentó llevar seguimiento con **Microsoft Planner** y **Microsoft
Loop**. No funcionó. La causa no fueron las herramientas sino el desbalance de
esfuerzo: **el que escribe no es el que consume**. Cargar una tarjeta le cuesta
a quien ejecuta y le sirve a quien coordina, y eso termina en abandono.

A eso se suma la fricción de saltar entre aplicaciones. El trabajo diario está
centralizado en:

- **Outlook** — comunicación.
- **Power BI** — herramienta principal de entrega.
- **Claude Desktop / VS Code** — desarrollo de los Megamente y documentación de
  proyecto, trabajando directamente sobre las carpetas de OneDrive.
- **Teams** — centraliza las carpetas compartidas por cliente.

Cualquier herramienta que exija abrir una quinta aplicación va a correr la misma
suerte que Planner y Loop.

## 2. Qué cambió

Ahora **no escribe el humano, escribe Claude**. Las bitácoras y los archivos de
sprint del proyecto Krikos están mejor redactados que cualquier tarjeta de
Planner y no costaron esfuerzo de redacción. Ese es el activo sobre el que se
apoya todo lo demás.

## 3. Principios de diseño

1. **Nadie escribe para el tablero.** Si alguien tiene que abrir el sitio para
   actualizar un estado, se volvió a Planner. El tablero es 100% derivado de los
   archivos Markdown.
2. **La captura vive donde ya están.** El único momento de registro es el cierre
   de sesión en Claude Desktop o VS Code.
3. **El consumidor recibe, no busca.** Agustín vive en Outlook: el correo
   semanal es probablemente el entregable de mayor impacto, y el sitio es el
   respaldo navegable.
4. **Una sola fuente de verdad.** Los archivos Markdown en OneDrive. El sitio
   lee; no edita (con una única excepción controlada, ver sección 7).

## 4. Contexto del equipo

| Persona | Rol | Uso de Claude |
|---|---|---|
| Fernando Perulan | Consultor — Frente B en Krikos | Desarrollo, documentación, VS Code |
| Juan Manuel Daher (JMD) | Consultor — Frente A en Krikos | Desarrollo y documentación |
| Guido | Visualización y métricas de Power BI | Definición y creación de métricas |
| Agustín | Head of projects | Registro, preguntas conceptuales y de management |

Los cuatro tienen cuenta de Claude y las carpetas de OneDrive sincronizadas, así
que **los cuatro pueden generar registro automático**, no sólo los dos frentes
técnicos.

**Ritmo de trabajo**: reunión de planificación semanal los lunes. Cada proyecto
maneja además sus propios sprints con el cliente, normalmente de lunes a lunes.

## 5. Arquitectura

```
OneDrive (fuente de verdad)
  └── Inspirare Consulting/
        ├── LoPresti Posca - Documents/
        │     └── PO_LP_26_Krikos-Compras-FillRate/
        │           ├── CLAUDE.md
        │           ├── objetivos_kickoff.md
        │           ├── Seguimiento/
        │           │     ├── Bitacora_Fernando.md
        │           │     ├── Lineamientos.md
        │           │     └── Sprints/
        │           └── COMPRAS/ , FILL RATE/ , KRIKOS/ ...
        ├── SAUDA SRL - Documents/
        └── Grupo CARBONERO - Documents/
                    │
                    ▼
        Recolector (GitHub Actions, programado)
          · Lee vía Microsoft Graph API
          · Parsea front matter + checkboxes
          · Genera state.json
                    │
         ┌──────────┴──────────┐
         ▼                     ▼
   Sitio estático        Correo semanal
   (GitHub Pages)        (Graph API → Outlook)
```

**Decisión de hosting**: GitHub Actions + GitHub Pages. No hace falta Vercel ni
ninguna plataforma adicional — el repo ya da build, hosting, historial y
permisos.

**Alternativas evaluadas y descartadas para la v1**:

- *Repo git como fuente de verdad en lugar de OneDrive*: es lo más robusto y da
  historial real, pero obliga a Guido y Agustín a convivir con git. Queda como
  destino natural si el equipo se adapta.
- *Edición desde la web*: genera dos fuentes de verdad y pudre el sistema.

## 6. Contrato de datos

La estructura documental actual de Krikos es buena y no hace falta rehacerla.
Faltan tres cosas para que sea legible por máquina.

### 6.1 Front matter

Cinco campos, no quince. En archivos de sprint y bitácoras:

```yaml
---
frente: B
tipo: sprint          # sprint | bitacora | entregable
estado: en_curso      # no_iniciado | en_curso | bloqueado | hecho
responsable: Fernando
hito: 2026-09-15
---
```

La prosa queda debajo, sin tocar. El parser sólo mira el front matter y los
checkboxes.

### 6.2 El hito bloqueante como objeto de primera clase

Es el concepto más fuerte de la documentación actual: cada sprint tiene uno, y el
Plan General ya identifica que el relevamiento con Lucas bloquea toda la cadena
del Frente B. Mostrar "hito bloqueante del sprint actual, estado, días abiertos"
por frente cubre la mayor parte de lo que necesita saber un head of projects, y
ninguna herramienta genérica modela esto.

### 6.3 Definición de hecho como checklist

Los criterios de "hecho" de cada sprint ya son binarios y están acordados con el
cliente. Escritos como `- [ ]` / `- [x]`, el avance del sprint se calcula solo,
sin que nadie estime nada. Evita la discusión de "¿vamos al 60 o al 70?".

### 6.4 Regla de escritura de bitácoras

A incorporar en `CLAUDE.md` antes de que se sumen más personas: **la bitácora
registra lo ocurrido, no lo planificado**. Los próximos pasos van en su propia
sección. Sin esta regla, el riesgo concreto es que quede registrado como hecho
lo que sólo se conversó.

## 7. El sitio

Prototipo funcional entregado: `sitio/index.html`. Una sola página, tema
oscuro, responsive para usar como web app en el celular.

**Vistas**:

1. **La semana** (inicio) — hitos bloqueantes abiertos, bloqueos y qué se movió,
   en todos los proyectos a la vez. Es lo primero que ve Agustín.
2. **Proyecto** — recorrido de los seis sprints con los dos frentes en carriles
   paralelos y el sprint activo marcado; tarjeta por frente con hito bloqueante y
   avance; riesgos; bitácora completa.
3. **Correo del lunes** — selección de qué secciones entran, con vista previa en
   vivo y configuración de destinatarios y horario.
4. **Lineamientos** — única entrada de datos del sitio.

**Decisiones tomadas en el prototipo**:

- El estado vacío es deliberadamente incómodo: si nadie registró nada, el panel
  dice que faltó correr el cierre de sesión. Eso es información, no un error.
- Los lineamientos escriben en modo *append-only*: agregan un bloque al final de
  `Seguimiento/Lineamientos.md`, nunca modifican lo existente. Un append no puede
  corromper lo que ya estaba.

## 8. Robustez

La forma de evitar datos erróneos no es validar en el sitio, sino que **nunca
haya dos fuentes de verdad**. El recolector lee, el sitio muestra.

Para el bot de audio (etapa 5), el riesgo real es que una transcripción tomada
en la calle meta ruido en la bitácora. Mitigación: el bot no escribe directo —
devuelve el borrador estructurado por chat y espera confirmación antes de
guardar. Dos segundos de fricción que evitan una bitácora con datos inventados.

## 9. Roadmap

**Etapa 1 — Contrato de datos** *(desbloquea todo lo demás)*
- Definir el front matter y aplicarlo a los archivos existentes de Krikos.
- Convertir las definiciones de hecho a checkboxes.
- Escribir el comando `/cierre` en `.claude/commands/` para que Claude mantenga
  el formato sin que el equipo piense en él.
- Agregar a `CLAUDE.md` la regla de bitácora de la sección 6.4.

**Etapa 2 — Recolector**
- App registration en Azure, permisos `Files.Read.All`.
- Script que lea las carpetas vía Graph API, parsee y genere `state.json`.
- GitHub Action programada.

**Etapa 3 — Publicación**
- Sitio en GitHub Pages alimentado por `state.json`.
- Correo semanal por Graph API, lunes a la mañana antes de la reunión.

**Etapa 4 — Entrada de lineamientos**
- Escritura append-only desde el sitio vía Graph API.

**Etapa 5 — Captura por voz**
- Bot de WhatsApp o Telegram que reciba audios, transcriba, estructure y
  confirme por chat antes de escribir.

## 10. Cómo validar si esto funciona

La v1 más chica que prueba la hipótesis **no es el sitio**: es el comando de
cierre, el front matter y el correo semanal. Si en tres semanas eso sobrevive sin
que nadie lo fuerce, el sitio se justifica solo. Si nadie corre el comando de
cierre, el sitio hubiera sido trabajo perdido igual.

## 11. Estructura de repo propuesta

```
panel-inspirare/
├── README.md
├── docs/
│   ├── 00_Panel_Seguimiento.md      ← este documento
│   ├── contrato-datos.md            ← front matter y convenciones
│   └── decisiones/                  ← registro de decisiones de arquitectura
├── recolector/
│   ├── graph_client.py
│   ├── parser.py
│   └── build_state.py
├── sitio/
│   ├── index.html
│   └── state.json                   ← generado, no editar a mano
├── mail/
│   └── digest.py
├── .claude/
│   ├── commands/cierre.md
│   └── CLAUDE.md
└── .github/workflows/
    ├── recolectar.yml
    └── digest-lunes.yml
```

---

## Pendiente de decidir

- Si el correo semanal cubre todos los proyectos en un solo envío o uno por
  proyecto.
- Qué pasa con los proyectos que todavía no tienen la carpeta estandarizada
  (Carbonero está en pausa; SAUDA tiene estructura propia).
- Si Guido y Agustín corren el comando de cierre en sus propias sesiones o si su
  registro se deriva de otra forma.
- **Identidad y perfil de usuario** (planteado 2026-09-11): el sitio debería
  identificar quién lo está mirando y mostrarle en un perfil sus propios
  movimientos recientes. Análisis completo en
  [`docs/decisiones/002-login-y-control-de-acceso.md`](decisiones/002-login-y-control-de-acceso.md)
  — falta decidir si alcanza con identificar (GitHub Pages + MSAL.js) o hace
  falta restringir acceso de verdad (migrar a Azure Static Web Apps).
- **Carpeta de Inspirare Consulting (no por cliente)**: propuesta completa en
  [`docs/estructura-organizacional.md`](estructura-organizacional.md).
  Pendiente de confirmar con el equipo si `Inspirare Ops` (Teams) es la
  carpeta de compañía, o si se usa otra.
- **Teams (chat y canales)**: la empresa ya tiene equipos de Teams por
  cliente con chats y canales armados, pero hoy no se usan — se intentó antes
  de que Fernando se sumara y no funcionó. No se considera como canal de
  captura ni de entrega para este proyecto.
- **WhatsApp / correo semanal**: confirmado como dirección a futuro (ya
  cubierto por la Etapa 3 — correo — y la Etapa 5 — bot de WhatsApp — de
  este roadmap). No es una etapa nueva, sólo una confirmación.