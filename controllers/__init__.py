from .users_controller import UsersController
from .dealership_controller import DealershipController
from .sellers_controller import SellersController
from .cars_controller import CarsController
from .car_types_controller import CarTypesController
from .car_photos_controller import CarPhotosController
from .car_features_controller import CarFeaturesController
from .car_feature_values_controller import CarFeatureValuesController
from .feature_options_controller import FeatureOptionsController
from .comments_controller import CommentsController
from .reviews_controller import ReviewsController

# Initialize controllers
users_controller = UsersController()
dealership_controller = DealershipController()
sellers_controller = SellersController()
cars_controller = CarsController()
car_types_controller = CarTypesController()
car_photos_controller = CarPhotosController()
car_features_controller = CarFeaturesController()
car_feature_values_controller = CarFeatureValuesController()
feature_options_controller = FeatureOptionsController()
comments_controller = CommentsController()
reviews_controller = ReviewsController()
