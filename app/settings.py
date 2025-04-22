import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "gemini_app")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

LLM_MODEL_NAME = "gemini-2.0-flash-001"
