# Onboarding — cliente nuevo

Checklist para arrancar un proyecto sin inventar la estructura de nuevo cada
vez. Ver `docs/estructura-organizacional.md` en el repo del panel para el
razonamiento completo detrás de cada paso.

## Antes del kick off

- [ ] Crear `<Cliente> - Documents/` en OneDrive (o confirmar que ya existe
      si el cliente tiene un equipo de Teams previo).
- [ ] Copiar adentro la carpeta `Plantillas/` completa (con sus subcarpetas
      `Seguimiento/` y `Seguimiento/Sprints/`).
- [ ] Completar `CLAUDE.md` con el contexto del cliente.
- [ ] Completar `objetivos_kickoff.md`.
- [ ] Definir el reparto de frentes y quién lleva la bitácora de cada uno.

## En el kick off

- [ ] Repasar roadmap, alcance, forma de trabajo y próximos pasos (ver
      plantilla de `objetivos_kickoff.md`).
- [ ] Dejar escrito el Sprint 1 de cada frente, con hito bloqueante y
      definición de hecho, antes de que termine la semana.

## Después del kick off

- [ ] Agregar el proyecto a `recolector/proyectos.yml` en el repo del panel,
      para que el sitio lo empiece a leer.
- [ ] Agregar a la persona a `sitio/usuarios.json` (vía el secret
      `PANEL_USERS`) si todavía no tiene acceso al panel.
