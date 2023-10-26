from typing import List, Dict, Any

from fastapi import APIRouter, Query

from api.dependencies import RemoteUOW
from schemas.brands import BrandDTO
from services.brands import BrandService

router = APIRouter(
    prefix="/brands",
    tags=["Brands"]
)


@router.get("/", response_model=List[BrandDTO])
async def list(uow: RemoteUOW) -> list[BrandDTO]:
    return await BrandService().list(uow)


@router.get("/settings/", response_model=List[str])
async def params(uow: RemoteUOW, ) -> List[str]:
    return await BrandService().get_settings(uow)
