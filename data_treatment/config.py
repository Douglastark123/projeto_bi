import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file from project root
env_path = Path(__file__).resolve() / ".env"
load_dotenv(dotenv_path=env_path)

# === Environment Variables === #
DATASET_FILE  = os.getenv("DATASET_FILE")

# PostgreSQL
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_URL_PARAMS = os.getenv("POSTGRES_URL_PARAMS")
POSTGRES_TABLE = "veiculos_fipe"