import logging
import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from sqlalchemy.orm import Session
from app.routers import test_route

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    """Creates a FASTAPI app instance and mounts routes."""
    fast_application = FastAPI()
    fast_application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )
    fast_application.include_router(test_route.router)
    return fast_application


fast_app = create_application()

sio = socketio.AsyncServer(
    async_mode="asgi", cors_allowed_origins="*", logger=True, engineio_logger=True
)

app = socketio.ASGIApp(
    socketio_server=sio,
    other_asgi_app=fast_app,
)


@fast_app.on_event("startup")
async def startup_event():
    """Notify that application is starting"""
    log.info("starting....")
    return "starting..."


@fast_app.on_event("shutdown")
async def shutdown_event():
    """Notify that application is closing"""
    log.info("shutting down...")


@fast_app.get("/")
def read_root():
    """Tests the GET method on the root url"""
    return {"Hello": "World"}
