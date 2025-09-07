from typing import (
    Annotated,
    Union, List,
)

from fastapi import (
    APIRouter,
    Depends,
    Response,
    status, HTTPException,
)

from src.authentication.utils import get_current_user
from src.common.exceptions.base import ObjectDoesNotExistException

from src.common.schemas.common import ErrorResponse
from src.users.models.pydantic import UserAddressModel, UserModel, UserAddressModelDetail

from src.users.routes import UserRoutesPrefixes
from src.users.services import UserAddressService, get_user_address_service




router = APIRouter(prefix=UserRoutesPrefixes.address)


@router.get(
    UserRoutesPrefixes.root,
    responses={
        status.HTTP_200_OK: {'model': UserAddressModel},
        status.HTTP_404_NOT_FOUND: {'model': ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
    response_model=List[UserAddressModel],
)
async def user_address(
    current_user: Annotated[UserModel, Depends(get_current_user)],
    addresses_service: Annotated[UserAddressService, Depends(get_user_address_service)]
) -> List[UserAddressModel]:

    return await addresses_service.get_by_user_id(current_user.id)



@router.get(
    UserRoutesPrefixes.detail,
    responses={
        status.HTTP_200_OK: {'model': UserAddressModelDetail},
        status.HTTP_404_NOT_FOUND: {'model': ErrorResponse},
    },
    status_code=status.HTTP_200_OK,
    response_model=Union[UserAddressModelDetail, ErrorResponse],
)
async def address_detail(
    pk: int,
    current_user: Annotated[UserModel, Depends(get_current_user)],
    service: Annotated[get_user_address_service, Depends()],
) -> Union[UserAddressModelDetail, ErrorResponse]:

    try:
        address = await service.get_details(pk)
    except ObjectDoesNotExistException as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    if address.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    return UserAddressModelDetail.model_validate(address)