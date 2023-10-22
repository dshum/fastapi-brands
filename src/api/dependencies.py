from typing import Annotated

from fastapi import Depends

from services.unitofwork import IUnitOfWork, UnitOfWork

UOW = Annotated[IUnitOfWork, Depends(UnitOfWork)]

__all__ = ["UOW"]
