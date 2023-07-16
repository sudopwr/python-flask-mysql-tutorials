# usecases
# register routes

from main.usecases.products import products_api_bpl 
from main.usecases.login import login_api_bpl 
from main.usecases.orders import orders_api_bpl 

def register_route(app):
    app.register_blueprint(products_api_bpl)
    app.register_blueprint(login_api_bpl)
    app.register_blueprint(orders_api_bpl)
