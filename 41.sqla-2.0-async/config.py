__all__ = (
    "BASE_DIR",
    "DB_URL",
    "DB_ECHO",
)

from pathlib import Path

BASE_DIR = Path(__file__).parent

SQLITE_DB_PATH = BASE_DIR / "db.sqlite3"

DB_URL = f"sqlite+aiosqlite:///{SQLITE_DB_PATH}"
# DB_ECHO = False
DB_ECHO = True
