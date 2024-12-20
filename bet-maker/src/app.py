from fastapi import Depends, FastAPI

from src.api.routers.event_routers import event_routers
from src.app_di_container import AppDiContainer


def get_application() -> FastAPI:
    application = FastAPI()
    app_di_container = AppDiContainer()

    application.include_router(event_routers, dependencies=[Depends(lambda: app_di_container.bl_manager)])

    return application

app = get_application()
