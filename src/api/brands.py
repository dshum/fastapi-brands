from typing import List, Dict, Any

from fastapi import APIRouter, Query

from api.dependencies import UOW
from schemas.brands import BrandDTO
from services.brands import BrandService

router = APIRouter(
    prefix="/brands",
    tags=["Brands"]
)


@router.get("/", response_model=List[BrandDTO])
async def list(uow: UOW, params: List[str] = Query(None)) -> list[BrandDTO]:
    return await BrandService().list(uow, params)


@router.get("/{name}", response_model=BrandDTO)
async def get(uow: UOW, name: str) -> BrandDTO:
    return await BrandService().get(uow, name)


@router.get("/params/", response_model=List[str])
async def params(uow: UOW, ) -> List[str]:
    return await BrandService().get_params(uow)
