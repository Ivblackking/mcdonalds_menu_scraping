import json
from fastapi import FastAPI, HTTPException, status


DATA_FILEPATH = "mc_menu_data_for_api.json"


app = FastAPI()


@app.get("/all_products/")
def get_all_products():
    with open(DATA_FILEPATH, "r", encoding="utf8") as file:
        all_products = json.load(file)
    return all_products


@app.get("/products/{product_name}")
def get_product(product_name:str):
    with open(DATA_FILEPATH, "r", encoding="utf8") as file:
        all_products = json.load(file)
        try:
            product = list(filter(lambda p: p["name"] == product_name, all_products))[0]
        except IndexError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Product with such name does not exist."
            )
    return product


@app.get("/products/{product_name}/{product_field}")
def get_product_field(product_name:str, product_field:str):
    with open(DATA_FILEPATH, "r", encoding="utf8") as file:
        all_products = json.load(file)
        try:
            product = list(filter(lambda p: p["name"] == product_name, all_products))[0]
            field_data = product[product_field]
        except IndexError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Product with such name does not exist."
            )
        except KeyError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid product field."
            )
    return field_data