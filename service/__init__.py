from .users_service import UserService
from .dealership_service import DealershipService
from .sellers_service import SellerService
from .cars_service import CarService
from .car_types_service import CarTypeService
from .car_features_service import CarFeatureService
from .feature_options_service import FeatureOptionService
from .car_feature_values_service import CarFeatureValueService
from .car_photos_service import CarPhotoService
from .comments_service import CommentService
from .reviews_service import ReviewService


users_service = UserService()
dealerships_service = DealershipService()
sellers_service = SellerService()
cars_service = CarService()
car_types_service = CarTypeService()
car_features_service = CarFeatureService()
feature_options_service = FeatureOptionService()
car_feature_values_service = CarFeatureValueService()
car_photos_service = CarPhotoService()
comments_service = CommentService()
reviews_service = ReviewService()

