from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    from app.root import register_routes
    from root.autodoc import openapi_bp, swagger_ui_bp
    app.register_blueprint(openapi_bp)
    app.register_blueprint(swagger_ui_bp, url_prefix="/docs")
    register_routes(app)

    return app
