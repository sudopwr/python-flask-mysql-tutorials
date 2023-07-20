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

@products_api_bpl.route("/products/<id>", methods=["get"])
def get_product_by_id(id):
    try:
        product = Product.query.get(id)
        return jsonify(product), 200
    except:
        return {"message": "Failed to add product"}, 400

@products_api_bpl.route("/products/<id>", methods=["delete"])
@login_required
@should_admin
def update_product(id):
    try:
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return '', 200
    except:
        return {"message": "Failed to delete product"}, 400

@products_api_bpl.route("/products/<id>", methods=["put"])
@login_required
@should_admin
def delete_product_by_id(id):
    try:
        request_json = request.get_json()
        product = Product.query.get_or_404(id)
        product.name=request_json["name"]
        product.price=request_json["price"]
        product.description=request_json["description"]
        product.quantity=request_json["quantity"]
        if "image" in request_json:
            product.image=request_json["image"]

        db.session.commit()
        return '', 200
    except Exception as e:
        print(e)
        return {"message": "Failed to update product"}, 400
