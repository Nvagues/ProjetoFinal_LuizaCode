import uvicorn
from fastapi import FastAPI
from rotas import order_items, orders, products, user_address, address, users
from server.database import db

app = FastAPI()
app.include_router(users.router)
app.include_router(products.router)
app.include_router(user_address.router)
app.include_router(address.router)
app.include_router(orders.router)
app.include_router(order_items.router)
app.add_event_handler("OFF", db.client.close())

if __name__ == '__main__':
    uvicorn.run("main:app", port=8000, reload=True, access_log=False)