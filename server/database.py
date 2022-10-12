from motor.motor_asyncio import AsyncIOMotorClient
import settings


class DataBase():
    connect: AsyncIOMotorClient = None
    product_db = None
    users_collection = None 
    address_collection = None 
    
database = DataBase()

async def connection_db():
    database.connect = AsyncIOMotorClient(settings.settings.DATABASE_URI)
    database.product_db = database.connect.Tintas.product
    db.users_collection = db.clients.luizaCode.users 
    db.address_collection = db.clients.luizaCode.address
    
    
    
async def connection_close():
    database.connect.close()
