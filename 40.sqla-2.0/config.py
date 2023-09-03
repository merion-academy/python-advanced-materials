__all__ = (
    "BASE_DIR",
)

from pathlib import Path

BASE_DIR = Path(__file__).parent

SQLITE_DB_PATH = BASE_DIR / "db.sqlite3"

DB_URL = f"sqlite:///{SQLITE_DB_PATH}"
# DB_ECHO = False
DB_ECHO = True
