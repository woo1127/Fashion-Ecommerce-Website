import sqlalchemy as sa
import sqlalchemy.orm as so
from apiflask import APIFlask
from utils import data_creator
from responses import error_response
from searcher.mixin import SearchableMixin
from searcher.searcher import WhooshSearcher
from extensions import db, jwt, cors, migrate
from werkzeug.exceptions import HTTPException
from config import Config, ProuctionConfig, DevelopmentConfig
from routes import auth_bp, product_bp, cart_bp, order_bp


def create_app(config_object=Config):
    app = APIFlask(__name__)
    app.json.sort_keys = False
    app.config.from_object(ProuctionConfig)
    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)
    register_shell_context(app)
    return app


def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(order_bp)


def register_extensions(app):
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    # https://stackoverflow.com/questions/24827857/flask-cors-wrapper-not-working-when-jwt-auth-wrapper-is-applied
    cors.init_app(
        app,
        resource={r"*": {"origins": "http://127.0.0.1:5173"}},
        allow_headers=["Content-Type", "Authorization", "X-CSRF-TOKEN", "cookie", "Access-Control-Allow-Credentials"],
        support_credentials=True
    )
    SearchableMixin.init_search(WhooshSearcher(app), db)
    

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def not_found(e):
        return error_response(e.code, e.description)


def register_shell_context(app):
    def make_shell_context():
        return {
            'app': app,
            'db': db,
            'sa': sa,
            'so': so,
            'create_data': data_creator,
        }
    app.shell_context_processor(make_shell_context)


if __name__ == '__main__':
    app = create_app()
    app.run()
