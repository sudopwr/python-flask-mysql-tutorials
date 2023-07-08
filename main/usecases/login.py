from flask import Blueprint, request, current_app
import jwt
from google.oauth2 import id_token
from google.auth.transport import requests
from flask_cors import cross_origin
import datetime

from main.models import User
from main.extensions import db

login_api_bpl = Blueprint("Login", __name__)


@login_api_bpl.route("/login", methods=["post"])
@cross_origin()
def verify():
    request_json = request.get_json()
    google_jwt = request_json["jwt"]
    try:
        id_info = id_token.verify_oauth2_token(
            google_jwt, requests.Request(), current_app.config['GOOGLE_CLIENT_ID'])
        google_user_id = id_info["sub"]
        user = User.query.get(google_user_id)
        if user is None:
            user = User(
                id=google_user_id,
                name=id_info["name"],
                email=id_info["email"],
                address="",
                image=id_info["picture"]
            )
            db.session.add(user)
            db.session.commit()

        payload = {
            "id": google_user_id,
            "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=1)
        }

        if current_app.config['ADMIN_EMAIL']:
            payload["role"] = "admin"

        user_jwt = jwt.encode(
            payload, current_app.config["JWT_SECRET"], algorithm="HS256")
        return {"token": user_jwt}
    except ValueError:
        return {"message": "Invalid request"}, 400
