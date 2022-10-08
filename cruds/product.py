from server.database import database
from models.product import ProductModel

def create_product(product: ProductModel):
    product = database.product_db.insert_one(product)
    
    return product

def get_products():
    products=database.product_db.find() #buscando no banco com o find 
    return products

    