from typing import (
    Annotated,
    Union,
)

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    Response,
    status,
)

from src.catalogue.models.database import Product, Category
from src.catalogue.routes import (
    CatalogueRoutesPrefixes,
    ProductRoutesPrefixes,
)
from src.catalogue.services import get_product_service, get_category_service
from src.common.enums import TaskStatus
from src.general.schemas.task_status import TaskStatusModel


router = APIRouter(prefix=CatalogueRoutesPrefixes.category)


@router.get(
    ProductRoutesPrefixes.root,
    status_code=status.HTTP_200_OK,
    response_model=list[Category],
)
async def category_list(category_service: Annotated[get_category_service, Depends()]) -> list[Category]:
    """
    Get list of products.

    Returns:
        Response with list of products.
    """
    return await category_service.list()



@router.get(
    ProductRoutesPrefixes.search,
    status_code=status.HTTP_200_OK,
)
async def search(
    keyword: str,
    service: Annotated[get_category_service, Depends()],
):
    """
    Search products.

    Returns:
        Response with products.
    """
    response = await service.search(keyword=keyword)

    return response


@router.post(
    ProductRoutesPrefixes.update_index,
    status_code=status.HTTP_200_OK,
)
async def update_elastic(
    background_tasks: BackgroundTasks,
    service: Annotated[get_category_service, Depends()],
):
    """
    Update products index.

    Returns:
        None.
    """
    status_model = await TaskStatusModel(status=TaskStatus.IN_PROGRESS).save_to_redis()

    background_tasks.add_task(service.update_category_index, status_model.uuid)

    return await TaskStatusModel().get_from_redis(uuid=status_model.uuid)
