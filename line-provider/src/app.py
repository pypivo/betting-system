from fastapi import Depends, FastAPI

from src.api.routers.event_routers import event_routers
from src.app_manager_container import AppManagerContainer
from src.bl.managers.manager import BLManager

def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan_context)

    app.include_router(event_routers)

    return app

async def lifespan_context(app: FastAPI):
    app_manager_container = AppManagerContainer()
    await app_manager_container.init_managers()

    app.dependency_overrides.update({
        BLManager: lambda: app_manager_container.bl_manager,
    })

    yield

app = create_app()
