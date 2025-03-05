from rococo.data import PostgreSQLAdapter
from app.config import DATABASE_CONFIG

db = None

def init_db():
    global db
    db = PostgreSQLAdapter(
        DATABASE_CONFIG["host"],
        DATABASE_CONFIG["port"],
        DATABASE_CONFIG["user"],
        DATABASE_CONFIG["password"],
        DATABASE_CONFIG["database"],
    )
    print("Database connected")

if db is None:
    init_db()

