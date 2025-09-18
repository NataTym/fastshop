from typing import (
    Annotated,
    Union, List,
)

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)

from src.catalogue.models.database import Product, AdditionalProducts, RecommendedProducts
from src.catalogue.routes import (
    CatalogueRoutesPrefixes,
    ProductRoutesPrefixes,
)
from src.catalogue.services import get_product_service, get_additional_product_service, get_recommended_product_service
from src.common.exceptions.base import ObjectDoesNotExistException
from src.common.schemas.common import ErrorResponse


router = APIRouter(prefix=CatalogueRoutesPrefixes.product)


@router.get(
    ProductRoutesPrefixes.root,
    status_code=status.HTTP_200_OK,
    response_model=list[Product],
)
async def product_list(product_service: Annotated[get_product_service, Depends()]) -> list[Product]:
    """
    Get list of products.

    Returns:
        Response with list of products.
    """
    return await product_service.list()


@router.get(
    ProductRoutesPrefixes.detail,
    responses={
        status.HTTP_200_OK: {'model': Product},
        status.HTTP_404_NOT_FOUND: {'model': ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
    response_model=Union[Product, ErrorResponse],
)
async def product_detail(
    response: Response,
    pk: int,
    service: Annotated[get_product_service, Depends()],
) -> Union[Response, ErrorResponse]:
    """
    Retrieve product.

    Returns:
        Response with product details.
    """
    try:
        response = await service.detail(pk=pk)
    except ObjectDoesNotExistException as exc:
        response.status_code = status.HTTP_404_NOT_FOUND
        return ErrorResponse(message=exc.message)

    return response


@router.get(
    ProductRoutesPrefixes.additional,
    responses={
        status.HTTP_200_OK: {'model': AdditionalProducts},
        status.HTTP_404_NOT_FOUND: {'model': ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
    response_model=Union[AdditionalProducts, ErrorResponse],
)
async def additional_products(
    service: Annotated[get_additional_product_service, Depends()]) -> List[Product]:

    return service.list()


@router.get(
    ProductRoutesPrefixes.recommended,
    responses={
        status.HTTP_200_OK: {'model': RecommendedProducts},
        status.HTTP_404_NOT_FOUND: {'model': ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
    response_model=Union[RecommendedProducts, ErrorResponse],
)
async def recommended_products(
    service: Annotated[get_recommended_product_service, Depends()]) -> Union[Response, ErrorResponse]:

    return service.list()



@router.post(
    "/products/{product_id}/additional/{additional_id}",
    response_model=AdditionalProducts,
    status_code=status.HTTP_201_CREATED,
)
async def add_additional_product(
    product_id: int,
    additional_id: int,
    service: Annotated[get_additional_product_service, Depends()]
):
    obj = AdditionalProducts(primary_id=product_id, additional_id=additional_id)
    return await service.create(obj)