from api.routers import message_router

from fastapi import FastAPI

def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(message_router)
    return application

app = get_application()