from pydantic import BaseModel, Field
from bson import ObjectId

class ProductModel(BaseModel):
    nome: str = Field(max_length=100)
    description: str
    marca:str
    cor:str
    preco:float
    externa_ou_interna:str
    codigo: int
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "nome": "Tinta BoaParede Azul",
                "descricao": "Tinta líquida para pintar paredes",
                "marca": "BoaPArede",
                "cor": "azul",
                "preco": 50.0,
                "externa_ou_interna": "interna",
                "imagem": "None",
                "codigo": 190
            }
        }
  