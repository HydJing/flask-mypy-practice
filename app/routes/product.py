from flask import Blueprint, request
from typing import Dict

product_blueprint = Blueprint("product", __name__, url_prefix="/api/products")

@product_blueprint.route("/", methods=["POST"])
def create_product():
    # Simulating incoming JSON data with product info
    data = request.get_json()  # Expected to be a dict

    # Mistakenly trying to index the data as if it's a list
    product_name = data[0]["name"]  # Error: Expecting a dict, treating it as a list

    return f"Product {product_name} created!", 201
