from flask import Flask, request,jsonify
from data import products_data, categories_data, brands_data

app = Flask(__name__)


@app.route("/")
def index():
    return "welcome"

@app.route("/products")
def get_products():
    return products_data

@app.route("/categories")
def get_categories():
    return categories_data

@app.route("/brands")
def get_brands():
    return brands_data

@app.route("/brands", methods=["POST"])
def create_brand():
    brands_details=request.get_json()
    print(brands_details)
    brands_data.append(brands_details["brand_name"])
    return{"message":"New Brand added Successfully"}

@app.route("/categories", methods=["POST"])
def create_category():
    categories_details=request.get_json()
    print(categories_details)
    brands_data.append(categories_details["category_name"])
    return{"message":"New category added Successfully"}