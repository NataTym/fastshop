from fastapi import Depends

from src.catalogue.models.database import Product, RecommendedProducts, AdditionalProducts
from src.catalogue.repository import (
    ProductRepository,
    get_product_repository, AdditionalProductRepository, RecommendedProductRepository,
    get_additional_product_repository, get_recommended_product_repository,
)
from src.common.service import BaseService


class ProductService(BaseService[Product]):
    def __init__(self, repository: ProductRepository):
        super().__init__(repository)


def get_product_service(repo: ProductRepository = Depends(get_product_repository)) -> ProductService:
    return ProductService(repository=repo)



class AdditionalProductService(BaseService[AdditionalProducts]):
    def __init__(self, repository: AdditionalProductRepository):
        super().__init__(repository)


def get_additional_product_service(repo: AdditionalProductRepository = Depends(get_additional_product_repository)) -> AdditionalProductService:
    return AdditionalProductService(repository=repo)


class RecommendedProductService(BaseService[RecommendedProducts]):
    def __init__(self, repository: RecommendedProductRepository):
        super().__init__(repository)


def get_recommended_product_service(repo: RecommendedProductRepository = Depends(get_recommended_product_repository)) -> RecommendedProductService:
    return RecommendedProductService(repository=repo)