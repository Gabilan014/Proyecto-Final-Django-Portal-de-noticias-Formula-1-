# Noticias F1 - Mini Portal

Descripción
---
Mini portal en Django que muestra noticias de Fórmula 1. Carga noticias desde una API (fallback a JSON local) y provee vistas para listar y ver detalles.

Requisitos
---
- Python 3.10+ (o el que uses)
- Git (opcional)
- Entorno virtual recomendado

Instalación y ejecución (Windows)
---
1. Abrir PowerShell en la raíz del proyecto (donde está `manage.py`).

2. Crear y activar entorno virtual:
```powershell
py -3 -m venv .venv
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
.\.venv\Scripts\Activate.ps1
```

(O en CMD:)
```cmd
py -3 -m venv .venv
.\.venv\Scripts\activate.bat
```

3. Instalar dependencias:
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

4. Crear archivo `.env` en la raíz (ejemplo):
```env
SECRET_KEY=replace-this-with-a-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///./db.sqlite3
RAPIDAPI_KEY=YOUR_RAPIDAPI_KEY_HERE
NOTICIAS_LOCAL_PATH=noticias/data/noticias.json
```
No subir `.env` al repositorio.

5. Migraciones y correr servidor:
```powershell
python manage.py migrate
python manage.py runserver
```

Acceder en el navegador:
http://127.0.0.1:8000/

JSON local de noticias
---
Si la API remota falla, el servicio usa `noticias/data/noticias.json`. Asegurate que el archivo sea JSON válido y contenga una lista de objetos con campos como `headline`, `description`, `link` e `images` (opcional).

Comprobaciones útiles
---
- Verificar que `requests`, `whitenoise`, `dj-database-url` (si lo usás) estén instalados.
- Activar el intérprete correcto en VS Code (Ctrl+Shift+P → Python: Select Interpreter).
- Para probar la carga de noticias desde shell:
```powershell
python manage.py shell
from noticias.services import get_f1_news
print(len(get_f1_news()))
```

Problemas comunes
---
- Si PowerShell bloquea la activación: ejecutar `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force`.
- Si falta un paquete: `python -m pip install <paquete>`.

