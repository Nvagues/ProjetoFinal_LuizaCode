from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
load_dotenv()


class DataBase():
    connect: AsyncIOMotorClient = None
    product_db = None
    order_items_db = None
    cart_db = None


database = DataBase()


def connection_db():
    database.connect = AsyncIOMotorClient(os.environ["DATABASE"])

    database.product_db = database.connect.Cluster0.product
    database.order_items_db = database.connect.Cluster0.order_items
    database.cart_db = database.connect.Cluster0.cart


def connection_close():
    database.connect.close()


connection_db()
