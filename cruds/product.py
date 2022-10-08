from server.database import database
from models.product import ProductModel

def create_product(product: ProductModel):
    product = database.product_db.insert_one(product.dict()) 
    print(product)
    return product

pr = {
    "nome":"Teste",
    "marca": "Suvinil",
    "cor":"Azul",
    "preco":150.00,
    "externa_ou_interna":"interna",  
     
}
produto = create_product(pr)
    