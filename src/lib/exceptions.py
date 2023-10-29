from fastapi import Request

from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import ValidationException

__all__ = ["exception_handlers"]


async def validation_exception_handler(request: Request, exc):
    return await request_validation_exception_handler(request, exc)


def exception_handlers():
    return {
        ValidationException: validation_exception_handler,
    }
