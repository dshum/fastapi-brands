from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import routers
from lib import settings, database, sentry, cache
from lib.exceptions import exception_handlers
from lib.ssh import server


@asynccontextmanager
async def lifespan(app: FastAPI):
    sentry.configure()
    cache.configure()
    server.start()
    await database.startup()
    yield
    server.stop()


app = FastAPI(
    debug=settings.app.DEBUG,
    exception_handlers=exception_handlers(),
    lifespan=lifespan,
)

for router in routers:
    app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", tags=["Default"])
async def hello(request: Request):
    return templates.TemplateResponse("hello.html", context={"request": request})
