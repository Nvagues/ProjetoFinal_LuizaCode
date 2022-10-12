from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
import settings


class DataBase():
    connect: AsyncIOMotorClient = None
    product_db = None
    users_collection = None 
    address_collection = None
    cart_db = None
    
database = DataBase()

async def connection_db():
    database.connect = AsyncIOMotorClient(settings.settings.DATABASE_URI)
    database.product_db = database.connect.Tintas.product
    database.users_collection = database.clients.luizaCode.users 
    database.address_collection = database.clients.luizaCode.address
    
    
    
async def connection_close():
    database.connect.close()

    
connection_db()
