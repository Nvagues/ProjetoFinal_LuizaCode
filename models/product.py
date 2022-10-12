from pydantic import BaseModel, Field

class ProductModel(BaseModel):
    nome:str
    marca:str
    cor:str
    preco:float
    externa_ou_interna:str
    
