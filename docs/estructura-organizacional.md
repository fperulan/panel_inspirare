---
proyecto: Panel de Seguimiento Inspirare
tipo: propuesta de estructura
estado: propuesta, sin aprobar
fecha: 2026-09-11
---

# Estructura de carpetas — Inspirare Consulting en OneDrive

Propuesta para que la carpeta compartida de la empresa (`Inspirare Consulting`
en OneDrive, hoy sincronizada también en cada equipo de Teams) tenga una
convención estable, sin necesidad de reorganizar de golpe lo que ya existe.
Complementa el contrato de datos (`contrato-datos.md`), que define el *formato*
de los archivos; este documento define *dónde viven*.

## 0. Lo que hay hoy (relevado 2026-09-11)

```
Inspirare Consulting/
├── Documentación de Desarrollo/        ← creada por Fernando al ingresar, uso poco claro
├── Grupo CARBONERO - Documents/        ← library de Teams del equipo "Grupo CARBONERO"
├── LoPresti Posca - Documents/         ← library de Teams del equipo "LoPresti Posca"
│     ├── 1. Diagnostico/
│     ├── 2. Desarrollo/
│     ├── Desarrollo/                   ← duplicado histórico de "2. Desarrollo"
│     ├── General/
│     ├── PO_LP_26_Krikos-Compras-FillRate/   ← el proyecto activo, ya con CLAUDE.md y Seguimiento/
│     ├── Proyectos BI/
│     └── Servicio Mantenimiento BI/
├── Panel Inspirare/                    ← este repo
├── SAUDA SRL - Documents/               ← library de Teams del equipo "SAUDA SRL"
│     ├── 4. Proyecto de Reorganización Empresarial 2023-2026/
│     ├── Capacitacion/, Desarrollo/, Diagnóstico/, General/
│     ├── Megamentes IA/, Proyecciones Demanda/
│     ├── SAUDA_Dashboard/, Tableros BI/, Tableros/
│     └── dataflow.png, SAUDA - Metodología Compra Inteligente.pdf (sueltos)
└── Test AZURE/
```

También existe el equipo de Teams **Inspirare Ops** (`General/`,
`Megamentes IA/`, `Procesos/`, `Roles en Proyecto/`) — pero, igual que
`Documentación de Desarrollo`, **hace tiempo que no se usa**. No es un punto
de partida más limpio que el otro.

**Diagnóstico**: cada cliente acumuló su propia mezcla de carpetas por
categoría (Diagnóstico, Desarrollo, Tableros) y por proyecto
(Krikos-Compras-FillRate, Reorganización 2023-2026), sin una regla que separe
una cosa de la otra. Es resultado natural de varios años de uso sin
convención, sumado a herramientas que se probaron y quedaron a medio usar
(Planner, Loop, Teams) — no hace falta "arreglarlo" retroactivamente para
avanzar, ni reflotar ninguna de las dos carpetas viejas.

## 1. Decisión: carpeta de compañía nueva, sin historia previa

**Ni `Inspirare Ops` ni `Documentación de Desarrollo`** — ambas tienen meses
sin uso y arrastran contenido a medio terminar. Se crea una carpeta nueva,
directamente en OneDrive, hermana de las de cada cliente:

```
Inspirare Consulting/
├── 00 - Compañía/          ← nueva, arranca limpia desde acá
├── LoPresti Posca - Documents/
├── SAUDA SRL - Documents/
├── Grupo CARBONERO - Documents/
└── Panel Inspirare/
```

El prefijo `00 - ` es sólo para que ordene primero en la lista y el equipo la
encuentre sin buscar. **Nombre a confirmar** — se puede usar otro si a
Fernando o al resto del equipo les cierra más.

`Documentación de Desarrollo` queda como está, sin tocar — es la carpeta
personal de Fernando, no hace falta vaciarla ni migrarla para que esto
funcione.

## 2. Carpeta de compañía (`00 - Compañía/`)

```
00 - Compañía/
├── Roles-y-Responsabilidades.md   ← quién es quién, qué frente cubre cada persona
├── Procesos/
│   └── Ritmo-de-trabajo.md        ← cadencia de sprints, reunión semanal, cómo se cierra sesión
├── Onboarding-Cliente-Nuevo.md    ← checklist paso a paso para arrancar un proyecto
└── Plantillas/                    ← copia exacta de docs/plantillas/ de este repo (ver sección 4)
```

`Roles-y-Responsabilidades.md` y `Onboarding-Cliente-Nuevo.md` son insumo
directo del panel: si en el futuro el sitio quiere mostrar "quién cubre qué"
sin ir proyecto por proyecto, lee de acá.

`Plantillas/` no es una lista de archivos sueltos: es **la misma carpeta**
que `docs/plantillas/` en este repo, con sus subcarpetas (`Seguimiento/`,
`Seguimiento/Sprints/`) ya armadas — para arrancar un cliente nuevo, se
duplica esa carpeta entera dentro de `<Cliente> - Documents/` y se completan
los `[placeholders]`. Nadie arma la estructura a mano cada vez.

## 3. Carpeta por cliente (`<Cliente> - Documents/`)

Estructura objetivo para proyectos nuevos — **no implica reorganizar los
proyectos viejos de SAUDA o LP SA que ya funcionan así**:

```
<Cliente> - Documents/
├── CLAUDE.md                    ← contexto completo del cliente (como el de Krikos)
├── Seguimiento/
│   ├── Lineamientos.md
│   ├── Bitacora_<Persona>.md    ← una por persona con frente asignado
│   └── Sprints/
│       ├── 00_Plan_General_Sprints.md
│       └── Sprint_NN_<Frente>.md
├── <Proyecto activo>/           ← entregables, diseño, demos de ese proyecto puntual
└── Archivo/                     ← proyectos cerrados o diagnósticos viejos, fuera del recorrido activo
```

Un cliente puede tener más de un `<Proyecto activo>/` en paralelo (ej. LP SA
podría sumar "Proyectos BI" como proyecto propio, separado de Krikos, cada uno
con su hito bloqueante). Lo que no debería pasar es una carpeta de categoría
genérica ("Desarrollo", "Tableros") sin dueño ni fecha — si algo no tiene
sprint activo ni bitácora, entra en `Archivo/`.

**Adopción incremental**: cuando arranca un proyecto nuevo, se crea con esta
estructura desde el día uno (copiando `Plantillas/`). Los proyectos viejos se
migran sólo si alguien los retoma activamente — no hace falta un trabajo de
migración aparte.

## 4. Plantillas

Viven en este repo, en [`docs/plantillas/`](plantillas/), no sólo en OneDrive
— así el contrato de datos (`contrato-datos.md`) y las plantillas nunca se
desalinean entre sí. La copia en `00 - Compañía/Plantillas/` es solo para que
el equipo las encuentre sin abrir git.

## 5. Cómo esto conecta con el recolector (Etapa 2)

El recolector necesita saber qué carpetas leer sin tener la ruta de OneDrive
hardcodeada en el código. Cuando se construya, la lista de clientes/proyectos
activos debería vivir en un manifiesto versionado (ver
`recolector/proyectos.yml`, creado como stub) — agregar un cliente nuevo es
agregar una entrada ahí, no tocar código.

## Pendiente

- Confirmar el nombre de la carpeta nueva (acá propuesta como
  `00 - Compañía`) con Agustín/JMD/Guido antes de crearla — no hay apuro en
  que sea perfecta, pero conviene que el nombre no cambie una vez que el
  equipo empiece a usarla.
- Crear la carpeta en OneDrive y copiar `docs/plantillas/` adentro, en
  `Plantillas/`.
- Completar `Roles-y-Responsabilidades.md` y `Onboarding-Cliente-Nuevo.md`
  con contenido real — hoy son esqueletos en `docs/plantillas/` (ver
  sección 2), les falta que alguien del equipo los llene.
