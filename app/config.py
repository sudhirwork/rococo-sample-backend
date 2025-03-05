import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", 5432),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "database": os.getenv("DB_NAME", "mydatabase"),
}

API_VERSION = os.getenv("API_VERSION")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_HOURS = os.getenv("JWT_EXPIRE_HOURS")
JWT_REFRESH_EXPIRE_DAYS = os.getenv("JWT_REFRESH_EXPIRE_DAYS")

FRONTEND_URL=os.getenv("FRONTEND_URL")
EMAIL_SERVICE_URL=os.getenv("EMAIL_SERVICE_URL")