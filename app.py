import os
from cruds.product import create_product
from server.database import connection_db
from dotenv import load_dotenv
load_dotenv()

# Conecta com o banco
connection_db()

# Cria produto

pr = {
    "nome":"Teste",
    "marca": "Suvinil",
    "cor":"Azul",
    "preco":150.00,
    "externa_ou_interna":"interna",  
     
}

produto = create_product(pr)
