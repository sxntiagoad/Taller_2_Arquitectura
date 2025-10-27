from flask import Flask
from app.routes import api, web
def init_app():
    app = Flask(__name__)

    app.register_blueprint(api.bp, url_prefix='/api')
    app.register_blueprint(web.bp)
    return app