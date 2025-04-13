from flask import Flask
from app.routes.hello import hello_blueprint
from app.routes.user import user_blueprint
from app.routes.auth import auth_blueprint

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(hello_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)
    return app
