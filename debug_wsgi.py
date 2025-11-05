import traceback
import importlib

try:
    importlib.import_module("miniportal.wsgi")
    print("✅ miniportal.wsgi importado correctamente")
except Exception:
    traceback.print_exc()