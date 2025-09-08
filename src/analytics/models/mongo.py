from datetime import datetime
from typing import List

from beanie import Document
from pydantic import (
    BaseModel,
    Field
)


class ProductAnalytics(Document):
    product_id: int
    timestamp: datetime

    class Settings:
        name = 'analytics'