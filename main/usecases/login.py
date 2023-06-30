from flask import Blueprint, request, current_app
import jwt
from google.oauth2 import id_token
from google.auth.transport import requests

login_api_bpl = Blueprint("Login", __name__)


@login_api_bpl.route("/login", methods=["post"])
def verify():
    request_json = request.get_json()
    google_jwt = request_json["jwt"]
    try:
        id_info = id_token.verify_oauth2_token(google_jwt, requests.Request(), current_app.config['GOOGLE_CLIENT_ID'])
        user_jwt = jwt.encode({ "id": id_info["sub"] }, current_app.config['JWT_SECRET'], algorithms=['HS256'])
        return { "token": user_jwt }
    except ValueError:
        return { "message": "Invalid request" }, 400
