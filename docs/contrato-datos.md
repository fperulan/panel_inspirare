---
proyecto: Panel de Seguimiento Inspirare
tipo: contrato de datos
estado: pendiente de aplicar
---

# Contrato de datos

Lo que un proyecto tiene que cumplir en sus archivos Markdown para que el
recolector lo pueda leer. Ver `00_Panel_Seguimiento.md` sección 6 para el
razonamiento detrás de cada punto; este documento es la referencia normativa,
pensada para copiarse o citarse desde el `CLAUDE.md` de cada proyecto.

**Estado**: definido, todavía no aplicado a ningún proyecto real. Etapa 1 del
roadmap.

## 1. Front matter

Cinco campos, en archivos de sprint y bitácoras:

```yaml
---
frente: B
tipo: sprint          # sprint | bitacora | entregable
estado: en_curso      # no_iniciado | en_curso | bloqueado | hecho
responsable: Fernando
hito: 2026-09-15
---
```

La prosa del archivo queda debajo, sin tocar. El parser sólo lee el front
matter y los checkboxes — no interpreta el resto del texto.

## 2. Hito bloqueante

Cada sprint declara un hito bloqueante — el ítem que, si no se resuelve, frena
todo lo que sigue en ese frente. Se escribe en prosa dentro del archivo de
sprint, bajo un encabezado `## Hito bloqueante` reconocible por el parser.

## 3. Definición de hecho como checklist

Los criterios de cierre del sprint se escriben como checkboxes de Markdown:

```markdown
## Definición de "hecho" del sprint

- [ ] Documento de reglas de negocio confirmado por Lucas
- [ ] Vista de Compras de Willy Mouse en mano, con documentación técnica
- [x] Gaps identificados entre lo que Lucas necesita y la vista actual
```

El avance del sprint se calcula contando `[x]` sobre el total. Nadie estima
manualmente un porcentaje.

## 4. Regla de escritura de bitácoras

La bitácora registra lo ocurrido, no lo planificado. Los próximos pasos van en
su propia sección (`## Próximos pasos` o equivalente), nunca mezclados con el
registro de lo ya hecho. Sin esta regla, el riesgo concreto es que quede
registrado como hecho lo que sólo se conversó.

Esta regla debe incorporarse al `CLAUDE.md` de cada proyecto antes de sumar
más gente al registro automático.

## Pendiente

- Aplicar el front matter a los archivos existentes del proyecto Krikos
  (ver `Modelo de proyecto real/` en este repo para una copia de referencia).
- Escribir el comando `/cierre` en `.claude/commands/` para que Claude
  mantenga el formato sin que el equipo tenga que pensar en él.
