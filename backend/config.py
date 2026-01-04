import os
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SQLite database path
DATABASE_PATH = BASE_DIR / "database" / "tron_music.db"

# Config dictionary (used later by our backend)
CONFIG = {
    "DATABASE_URL": f"sqlite:///{DATABASE_PATH}"
}
