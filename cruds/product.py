from server.database import database
from models.product import ProductModel

def create_product(product: ProductModel):
    product = database.product_db.insert_one(product)
    print(product)
    return product


    