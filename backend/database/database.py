from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv("API_URL"))

db = client[os.getenv("DATABASE")]

productos = db["productos"]
pedidos = db["pedidos"]
usuarios = db["usuarios"]