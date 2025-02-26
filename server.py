from flask import Flask, request, render_template
import json
from http import HTTPStatus
from config import db
from flask_cors import CORS


app = Flask(__name__)
CORS(app)# WARNING: THIS SIABLES CORS POLICY


@app.get("/")
def home():
    return "Hello from flask"


# @app.post("/")
# @app.put("/")
# @app.patch("/")


@app.get("/test")
def test():
    return "This is another endpoint"


# JSON implementation
@app.get("/api/about")
def about():
    name={"name":"Nick"}
    return json.dumps(name)


@app.get("/about-me")
def about_me():
    user_name = "Nick"
    return render_template("about-me.html", name=user_name)


products = []


def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj


#GET all products
@app.get("/api/products")
def get_products():
    products_db = []
    cursor = db.products.find({})
    for product in cursor:
        print("product ", product)
        products_db.append(fix_id(product))
    return json.dumps(products_db), HTTPStatus.OK


#POST/SAVE a product
@app.post("/api/products")
def save_product():
    item = request.get_json()
    db.products.insert_one(item)
    return json.dumps(fix_id(item))


##########################################
############# COUPON CODES ###############
##########################################


#post /api/coupons
@app.post("/api/coupons")
def save_coupon():
    item = request.get_json()
    db.coupons.insert_one(item)
    return json.dumps(fix_id(item))


#get /api/coupons
@app.get("/api/coupons")
def get_coupons():
    coupons_db = []
    cursor = db.coupons.find({})
    for coupons in cursor:
        print("Coupon ", coupons)
        coupons_db.append(fix_id(coupons))
    return json.dumps(coupons_db), HTTPStatus.OK

#coupon:
#code
#discount


#PUT a product
@app.put("/api/products/<int>index>")
def update_product(index):
    updated_product = request.get_json()
    print (f"update the product with index {index}")

    if 0 <= index < len(products):
        products[index] = updated_product
        return json.dumps(updated_product), 200
    else:
        return "That index does not exist", 404


#DELETE a product
@app.delete("/api/products/<int:index>")
def delete_product(index):
    print(f"delete the product with index {index}")

    if index >=0 and index < len(products):
        deleted_product = products.pop(index)
        return json.dumps(deleted_product)
    else:
        return "That index does not exist", HTTPStatus.NOT_FOUND


app.run(debug=True)

