from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv


class DataBase():
    connect: AsyncIOMotorClient = None
    product_db = None
    users_collection = None 
    address_collection = None order_items_db = None
    cart_db = None
    
database = DataBase()

async def connection_db():
    database.connect = AsyncIOMotorClient(settings.settings.DATABASE_URI)
    database.product_db = database.connect.Tintas.product
    db.users_collection = db.clients.luizaCode.users 
    db.address_collection = db.clients.luizaCode.address
    
    
    
async def connection_close():
    database.connect.close()

    
connection_db()

