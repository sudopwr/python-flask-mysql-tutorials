from flask import Blueprint

products_api_bpl = Blueprint("Products", __name__)

@products_api_bpl.route("/products")
def home():
    return "hello"
