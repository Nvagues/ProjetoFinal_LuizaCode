from motor.motor_asyncio import AsyncIOMotorClient
import settings


class DataBase():
    connect: AsyncIOMotorClient = None
    product_db = None
    
database = DataBase()

async def connection_db():
    database.connect = AsyncIOMotorClient(settings.settings.DATABASE_URI)
    database.product_db = database.connect.Tintas.product
    
async def connection_close():
    database.connect.close()