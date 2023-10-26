from typing import Annotated

from fastapi import Depends

from services.unitofwork import IUnitOfWork, LocalUnitOfWork, RemoteUnitOfWork

LocalUOW = Annotated[IUnitOfWork, Depends(LocalUnitOfWork)]
RemoteUOW = Annotated[IUnitOfWork, Depends(LocalUnitOfWork)]

__all__ = ["LocalUOW", "RemoteUOW"]
