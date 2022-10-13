from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from bson import json_util
import json

async def create_product(products_collection, product):
    data = jsonable_encoder(product)
    try:
        product = products_collection.insert_one(data)
        if product.inserted_id:
            product = await get_product(products_collection, product.inserted_id)
            return product
    except Exception as e:
        print(f'ERROR, {e}')

async def get_product(products_collection, product_id):
    try:
        product = products_collection.find_one({'_id': ObjectId(product_id)})
        if product:
            return json.loads(json_util.dumps(product))
    except Exception as e:
        print(f'ERROR, {e}')

async def get_products(products_collection, skip, limit):
    try:
        product_cursor = products_collection.find().skip(int(skip)).limit(int(limit))
        products = list(json.loads(json_util.dumps(product_cursor)))
        return products
    except Exception as e:
        print(f'ERROR, {e}')

async def update_product(products_collection, product_id, product_data):
    try:
        data = jsonable_encoder(product_data)

        product = products_collection.update_one(
            {'_id': ObjectId(product_id)},
            {'$set': {'price': data['price']}}
        )

        if product.modified_count:
            return True, product.modified_count

        return False, 0
    except Exception as e:
        print(f'ERROR, {e}')

async def delete_product(products_collection, product_id):
    try:
        product = products_collection.delete_one(
            {'_id': ObjectId(product_id)}
        )
        if product.deleted_count:
            return {'OK': 'OK'}
    except Exception as e:
        print(f'ERROR, {e}')