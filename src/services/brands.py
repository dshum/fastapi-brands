from datetime import datetime
from typing import Optional, List

from fastapi import HTTPException

from services.unitofwork import IUnitOfWork
from schemas.brands import BrandDTO


class BrandService:
    @staticmethod
    async def list(uow: IUnitOfWork):
        async with uow:
            brands = await uow.brands.list()
            return [BrandService.row_to_dto(**brand) for brand in brands]

    @staticmethod
    async def get_settings(uow: IUnitOfWork):
        async with uow:
            brands = await uow.brands.get_settings()
            params = []
            for brand in brands:
                params = params | brand[0].keys()
        return list(sorted(params))

    @staticmethod
    def row_to_dto(name: str, hosts: str, status: str, db_name: str,
                   created_at: datetime, updated_at: datetime, settings: str,
                   **kwargs) -> BrandDTO:
        return BrandDTO(
            name=name,
            hosts=hosts,
            status=status,
            db_name=db_name,
            created_at=created_at.strftime("%Y-%m-%d"),
            updated_at=updated_at.strftime("%Y-%m-%d"),
            settings=settings,
        )
