from functools import wraps
from flask import g, request, current_app
import jwt


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token, msg = get_token_auth_header()
        if token == False:
            return {"error": msg}, 401
        try:
            current_user = jwt.decode(
                token, current_app.config["JWT_SECRET"], algorithms=["HS256"])
            g.user = current_user
        except Exception as e:
            print(e)
            return {"error": "Invalid token"}, 401

        return f(*args, **kwargs)
    return decorated


def should_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            if g.user["role"] != "admin":
                return {"error": "Invalid request"}, 403
        except:
            return {"error": "Invalid request"}, 401

        return f(*args, **kwargs)
    return decorated

# https://auth0.com/blog/developing-restful-apis-with-python-and-flask/#Securing-Python-APIs-with-Auth0


def get_token_auth_header():
    auth = request.headers.get("Authorization", None)
    if not auth:
        return False, "Authorization header is expected"

    parts = auth.split()

    if parts[0].lower() != "bearer":
        return False, "Authorization header must start with Bearer"
    elif len(parts) == 1:
        return False, "Token not found"
    elif len(parts) > 2:
        return False, "Authorization header must be Bearer token"

    token = parts[1]
    return token, ''
