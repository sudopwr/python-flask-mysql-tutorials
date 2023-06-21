from main.modules.products import products_api_bpl 

def register_route(app):
    app.register_blueprint(products_api_bpl)
