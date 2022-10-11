
from pydantic import BaseModel, Field

class OrderItemsModel(BaseModel):
    id_product:str
    valor:float
    quantidade:int
        

    
