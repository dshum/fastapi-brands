from typing import List

from fastapi import APIRouter, Depends

from api.dependencies import LocalUOW
from lib.user import current_active_user
from schemas.brands import BrandDTO
from services.brands import BrandService

router = APIRouter(
    prefix="/brands",
    tags=["Brands"],
    dependencies=[Depends(current_active_user)]
)


@router.get("/", response_model=List[BrandDTO])
async def list(uow: LocalUOW) -> list[BrandDTO]:
    return await BrandService().list(uow)


@router.get("/settings/", response_model=List[str])
async def params(uow: LocalUOW, ) -> List[str]:
    return await BrandService().get_settings(uow)
