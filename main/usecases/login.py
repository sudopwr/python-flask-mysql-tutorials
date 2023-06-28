from flask import Blueprint

login_api_bpl = Blueprint("Login", __name__)


@login_api_bpl.route("/login", methods=["post"])
def verify():
    return "login"
