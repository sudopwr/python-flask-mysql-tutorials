from flask import Blueprint, request, jsonify, g
from main.models import Order, User, Product
from main.extensions import db
from main.utils import login_required, should_admin

orders_api_bpl = Blueprint("Orders", __name__)


@orders_api_bpl.route("/orders", methods=["post"])
@login_required
def add_order():
    try:
        request_json = request.get_json()
        order = Order(product_id=request_json["product_id"], user_id=g.user["id"],
                      quantity=request_json["quantity"], status="order_placed")
        db.session.add(order)
        db.session.commit()
        return '', 201
    except Exception as e:
        print(e)
        return {"message": "Failed to add order"}, 400


@orders_api_bpl.route("/orders", methods=["get"])
@login_required
@should_admin
def get_order():
    try:
        orders = Order.query\
            .join(User, Order.user_id == User.id)\
            .join(Product, Order.product_id == Product.id)\
            .add_columns(User.name, Product.name).all()
        result = []
        for order in orders:
            _order = order[0]
            _order = {
                "id": _order.id,
                "product_id": _order.product_id,
                "user_id": _order.user_id,
                "quantity": _order.quantity,
                "status": _order.status,
                "order_date": _order.order_date,
                "user_name": order[1],
                "product_name": order[2]
            }
            result.append(_order)

        return jsonify(result), 200
    except:
        return {"message": "Failed to get order"}, 400


@orders_api_bpl.route("/orders/user", methods=["get"])
@login_required
def get_users_orders():
    try:
        orders = Order.query\
            .join(User, Order.user_id == User.id)\
            .join(Product, Order.product_id == Product.id)\
            .add_columns(User.name, Product.name)\
            .filter(Order.user_id == g.user["id"]).all()
        result = []
        for order in orders:
            _order = order[0]
            _order = {
                "id": _order.id,
                "product_id": _order.product_id,
                "user_id": _order.user_id,
                "quantity": _order.quantity,
                "status": _order.status,
                "order_date": _order.order_date,
                "user_name": order[1],
                "product_name": order[2]
            }
            result.append(_order)

        return jsonify(result), 200
    except Exception as e:
        print(e)
        return {"message": "Failed to get order"}, 400


@orders_api_bpl.route("/orders/<id>", methods=["get"])
@login_required
@should_admin
def get_order_by_id(id):
    try:
        order = Order.query.get(id)
        return jsonify(order), 200
    except:
        return {"message": "Failed to get order"}, 400
