from datetime import datetime
from typing import Annotated

from fastapi import Depends

from src import analytics
from src.common.exceptions.base import ObjectDoesNotExistException
from src.common.service import BaseService
from src.analytics.models.mongo import (
    ProductAnalytics,
)
from src.analytics.repositories import ProductAnalyticsRepository


class ProductAnalyticsService(BaseService):
    def __init__(
        self,
        repository: Annotated[ProductAnalyticsRepository, Depends()],
    ):
        super().__init__(repository=repository)

    async def visit_record(self, product_id: int):
        analytics = ProductAnalytics(product_id = product_id, timestamp = datetime.now())

        await analytics.save()
