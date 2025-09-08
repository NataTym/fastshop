from src.common.repository.beanie import BaseMongoRepository
from src.analytics.models.mongo import ProductAnalytics


class ProductAnalyticsRepository(BaseMongoRepository[ProductAnalytics]):
    __model__ = ProductAnalytics