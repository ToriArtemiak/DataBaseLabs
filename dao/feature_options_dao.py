# feature_options_dao.py
from app.domain import FeatureOption
from app.dao.general_dao import GeneralDAO

class FeatureOptionDAO(GeneralDAO):
    _domain_type = FeatureOption
