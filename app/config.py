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

MAILJET_API_KEY = os.getenv("MAILJET_API_KEY")
MAILJET_SECRET_KEY = os.getenv("MAILJET_SECRET_KEY")
MAILJET_SENDER = os.getenv("MAILJET_SENDER")
FRONTEND_URL = os.getenv("FRONTEND_URL")
WELCOME_TEMPLATE_ID = os.getenv("WELCOME_TEMPLATE_ID")
RESET_TEMPLATE_ID = os.getenv("RESET_TEMPLATE_ID")