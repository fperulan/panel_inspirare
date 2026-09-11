"""Genera sitio/usuarios.json a partir del secret PANEL_USERS (JSON con
usuario/nombre/password en texto plano), hasheando cada contraseña con
SHA-256. Corre sólo dentro del workflow de publicación
(.github/workflows/deploy.yml) — el texto plano nunca se escribe a disco ni
se commitea, sólo vive en la variable de entorno durante este paso.

PANEL_USERS de ejemplo:
[{"usuario": "fernando", "nombre": "Fernando", "password": "..."}]
"""
import hashlib
import json
import os

usuarios = json.loads(os.environ["PANEL_USERS"])

salida = [
    {
        "usuario": u["usuario"],
        "nombre": u["nombre"],
        "hash": hashlib.sha256(u["password"].encode("utf-8")).hexdigest(),
    }
    for u in usuarios
]

with open("sitio/usuarios.json", "w", encoding="utf-8") as f:
    json.dump(salida, f, ensure_ascii=False, indent=2)
