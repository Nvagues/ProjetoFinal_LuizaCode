from server.database import database
from models.product import ProductModel

async def create_product(product: ProductModel):
    product = await database.product_db.insert_one(product)
    
    return product

async def get_products():
    products=database.product_db.find() #buscando no banco com o find 
    produtos = await products.to_list(length=10)
    return produtos

    