import asyncio
from cruds.product import create_product, get_products
from server.database import connection_db
from dotenv import load_dotenv
load_dotenv()

# Conecta com o banco
connection_db()

async def main():
    # Cria produto
    pr = {
        "nome":"Teste",
        "marca": "Suvinil",
        "cor":"Azul",
        "preco":150.00,
        "externa_ou_interna":"interna",  
     
    }

    # busca de produto
    #product = await create_product(pr)
    
    produtos = await get_products()
    print(produtos)

asyncio.run(main()) 