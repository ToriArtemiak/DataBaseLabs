# app/routes.py

from flask import Flask
from app.root.error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    # Register error handlers
    app.register_blueprint(err_handler_bp)

    # Import routers for each table in your database
    from .users_route import user_bp
    from .dealership_route import dealership_bp
    from .sellers_route import seller_bp
    from .cars_route import car_bp
    from .car_types_route import car_type_bp
    from .car_features_route import car_feature_bp
    from .feature_options_route import feature_option_bp
    from .car_feature_values_route import car_feature_value_bp
    from .car_photos_route import car_photo_bp
    from .comments_route import comment_bp

    # Register routers
    app.register_blueprint(user_bp)
    app.register_blueprint(dealership_bp)
    app.register_blueprint(seller_bp)
    app.register_blueprint(car_bp)
    app.register_blueprint(car_type_bp)
    app.register_blueprint(car_feature_bp)
    app.register_blueprint(feature_option_bp)
    app.register_blueprint(car_feature_value_bp)
    app.register_blueprint(car_photo_bp)
    app.register_blueprint(comment_bp)
