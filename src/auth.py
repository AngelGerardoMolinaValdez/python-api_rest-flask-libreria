from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
users = {"admin": "1234"}

@auth.verify_password
def verify_credentials(username, password):
    if username in users and users[username] == password:
        return username
