# Panel de Seguimiento — Inspirare Consulting

Panel de estado de proyectos derivado automáticamente de los archivos Markdown
que el equipo ya genera trabajando con Claude Desktop y VS Code. Nadie carga
datos a mano: el sitio lee, no escribe (con una única excepción controlada,
los lineamientos — ver la sección 7 del documento de traspaso).

El porqué completo, las decisiones tomadas y el roadmap están en
[`docs/00_Panel_Seguimiento.md`](docs/00_Panel_Seguimiento.md). Este README
solo orienta la navegación del repo.

## Estado actual

Prototipo de la interfaz (`sitio/index.html`) con datos de ejemplo embebidos.
Todavía no existe el recolector: el contrato de datos (front matter en los
archivos de proyecto) no está definido ni aplicado, así que no hay
`state.json` real.

Ver la sección **9. Roadmap** de `docs/00_Panel_Seguimiento.md` para las
etapas siguientes.

## Estructura del repo

```
docs/                   documentación del proyecto
  00_Panel_Seguimiento.md      documento de traspaso: problema, decisiones, roadmap
  contrato-datos.md            front matter y convenciones que debe cumplir un proyecto
  estructura-organizacional.md propuesta de estructura de carpetas en OneDrive
  decisiones/                  registro de decisiones de arquitectura (ADR)
  plantillas/                  CLAUDE.md, bitácora, sprints y lineamientos listos para copiar
sitio/
  index.html              interfaz del panel (hoy con datos de ejemplo embebidos)
  usuarios.example.json   ejemplo para probar el login en local (ver abajo)
  usuarios.json           [generado, gitignored] usuario/nombre/hash, lo arma el deploy
  state.json              [pendiente] generado por el recolector, no se edita a mano
scripts/
  build_usuarios.py       genera sitio/usuarios.json desde el secret PANEL_USERS
recolector/              [pendiente, Etapa 2] lee OneDrive vía Graph API y genera state.json
mail/                    [pendiente, Etapa 3] correo semanal por Graph API
.claude/
  CLAUDE.md               instrucciones de este repo para trabajar con Claude Code
  commands/cierre.md      [pendiente, Etapa 1] comando de cierre de sesión
.github/workflows/
  deploy.yml              publica sitio/ en GitHub Pages (genera usuarios.json)
  recolectar.yml          [pendiente, Etapa 2]
  digest-lunes.yml        [pendiente, Etapa 3]
Modelo de proyecto real/ copia de referencia del proyecto Krikos (LP SA) — no se
                          versiona (ver .gitignore), es fixture local para probar
                          el parser sin depender de Graph API
```

## Ver el prototipo

**En producción**: GitHub Pages (repo público), publicado por
`.github/workflows/deploy.yml` en cada push a `main` que toque `sitio/`.
Instructivo completo en [`docs/publicar-sitio.md`](docs/publicar-sitio.md).

**En local**: el sitio pide login, así que hace falta un `usuarios.json`.
Nunca commitear contraseñas reales acá — para probar:

```
cp sitio/usuarios.example.json sitio/usuarios.json   # usuario: admin — contraseña: 12345
cd sitio && python -m http.server 8000
```

Y abrir `http://localhost:8000`. Abrir el `index.html` con doble clic
(`file://`) no alcanza: el navegador bloquea el `fetch` de `usuarios.json` en
ese esquema.
