from .general_service import GeneralService
from ..dao import feature_options_dao


class FeatureOptionService(GeneralService):
    _dao = feature_options_dao
