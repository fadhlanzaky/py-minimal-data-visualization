from flask import Flask

from extensions.config_extension import register_configs
from extensions.exception_extension import register_exception_handler
from extensions.routes_extension import register_routes

def create_app():
    app = Flask(__name__)

    register_configs(app)
    register_routes(app)
    register_exception_handler(app)

    return app

