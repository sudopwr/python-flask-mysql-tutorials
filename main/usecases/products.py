from flask import Blueprint, request
from main.models import Product
from main.extensions import db

products_api_bpl = Blueprint("Products", __name__)


@products_api_bpl.route("/products", methods=["post"])
def add_product():
    try:
        request_json = request.get_json()
        product = Product(
            name=request_json["name"], price=request_json["price"], description=request_json["description"], quantity=request_json["quantity"], image='test.jpg')
        db.session.add(product)
        db.session.commit()
        return '', 201
    except:
        return {"message": "Failed to add product"}, 400
