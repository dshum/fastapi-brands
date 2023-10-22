from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import routers
from lib import settings, sentry, database
from lib.exceptions import exception_handlers

app = FastAPI(
    debug=settings.app.DEBUG,
    on_startup=(sentry.configure, database.startup),
    exception_handlers=exception_handlers()

)

for router in routers:
    app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def hello(request: Request):
    return templates.TemplateResponse("hello.html", context={"request": request})
