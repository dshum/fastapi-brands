from datetime import datetime
from typing import Optional, List

from fastapi import HTTPException

from services.unitofwork import IUnitOfWork
from schemas.brands import BrandDTO


class BrandService:
    @staticmethod
    async def list(uow: IUnitOfWork, params: Optional[List[str]] = None):
        if params is None:
            params = []
        async with uow:
            brands = await uow.brands.list_with_params(params)
            return [BrandService.row_to_dto(**dict(zip(["name", "hosts", "db_name", "created_at"] + params, brand)))
                    for brand in brands]

    @staticmethod
    async def get(uow: IUnitOfWork, name: str):
        async with uow:
            brand = await uow.brands.get_by_name(name)
            if not brand:
                raise HTTPException(status_code=404, detail="Brand not found")
            return brand.to_read_model()

    @staticmethod
    async def get_params(uow: IUnitOfWork):
        async with uow:
            brands = await uow.brands.list_with_settings()
            params = []
            for brand in brands:
                params = params | brand[0].keys()
        return list(sorted(params))

    @staticmethod
    def row_to_dto(name: str, hosts: str, db_name: str, created_at: datetime, **kwargs) -> BrandDTO:
        return BrandDTO(
            name=name,
            hosts=hosts,
            settings=kwargs,
            db_name=db_name,
            created_at=created_at.strftime("%Y-%m-%d"),
        )
