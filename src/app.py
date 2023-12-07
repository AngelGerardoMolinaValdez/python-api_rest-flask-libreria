from flask import Flask
from routes import initialize_routes

def create_app(test_config=None):
    app = Flask(__name__)
    initialize_routes(app)
    if test_config:
        app.config.update(test_config)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
