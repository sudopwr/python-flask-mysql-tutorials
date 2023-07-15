from flask import Blueprint, request, jsonify
from main.models import Product
from main.extensions import db
from main.utils import login_required, should_admin

products_api_bpl = Blueprint("Products", __name__)


@products_api_bpl.route("/products", methods=["post"])
@login_required
@should_admin
def add_product():
    try:
        request_json = request.get_json()
        product = Product(
            name=request_json["name"], price=request_json["price"], description=request_json["description"], quantity=request_json["quantity"], image=request_json["image"])
        db.session.add(product)
        db.session.commit()
        return '', 201
    except Exception as e:
        print(e)
        return {"message": "Failed to add product"}, 400


@products_api_bpl.route("/products", methods=["get"])
def get_product():
    try:
        products = Product.query.all()
        return jsonify(products), 200
    except:
        return {"message": "Failed to add product"}, 400
