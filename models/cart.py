from models.order_items import OrderItemsModel
from pydantic import BaseModel, Field

class CartModel(BaseModel):
    items:OrderItemsModel
    valor_total:float
    
    
    