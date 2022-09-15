from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
VENV_PATH = os.path.join(BASE_DIR)

print(VENV_PATH)
