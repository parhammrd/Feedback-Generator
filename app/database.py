from motor.motor_asyncio import AsyncIOMotorClient
from app.settings import MONGODB_URL, MONGODB_DB


client = AsyncIOMotorClient(MONGODB_URL)
db = client[MONGODB_DB]
