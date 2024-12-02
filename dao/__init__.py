# app/dao/__init__.py

from .users_dao import UserDAO
from .dealership_dao import DealershipDAO
from .sellers_dao import SellerDAO
from .cars_dao import CarDAO
from .car_types_dao import CarTypeDAO
from .car_features_dao import CarFeatureDAO
from .feature_options_dao import FeatureOptionDAO
from .car_feature_values_dao import CarFeatureValueDAO
from .car_photos_dao import CarPhotoDAO
from .comments_dao import CommentDAO
from .reviews_dao import ReviewDAO

# Import all DAOs here so they can be used in services and controllers
users_dao = UserDAO()
dealerships_dao = DealershipDAO()
sellers_dao = SellerDAO()
cars_dao = CarDAO()
car_types_dao = CarTypeDAO()
car_features_dao = CarFeatureDAO()
feature_options_dao = FeatureOptionDAO()
car_feature_values_dao = CarFeatureValueDAO()
car_photos_dao = CarPhotoDAO()
comments_dao = CommentDAO()
reviews_dao = ReviewDAO()
