from api import brands, users

__all__ = ["routers"]

routers = [
    users.router,
    brands.router,
]
