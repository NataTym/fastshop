from datetime import datetime
from typing import List

from beanie import Document
from pydantic import (
    BaseModel,
    Field
)


# class BaseProductAnalytics(BaseModel):
#     product_id: int
#     timestamp: datetime


# class ProductAnalytics(Document, BaseProductAnalytics):
#     visits: list[BaseProductAnalytics] =[]
#
#     class Settings:
#         name = 'analytics'


class BaseProductAnalytics(BaseModel):
    timestamp: datetime


class ProductAnalytics(Document):
    product_id: int
    visits: list[BaseProductAnalytics] = []

    class Settings:
        name = 'analytics'