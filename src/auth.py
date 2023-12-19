from flask_httpauth import HTTPBasicAuth
from models import users

auth = HTTPBasicAuth()

@auth.verify_password
def verify_credentials(username, password):
    user_data: list[dict[str, str]] = [
        user_data for user_data in users
        if user_data["username"] == username and user_data["password"] == password
    ]
    if user_data:
        return user_data[0]["username"]
