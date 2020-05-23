from fastapi import FastAPI, Depends

from . import https, sentry
from .routers import emails_router
from .security import api_key_checker

sentry.configure()

api = FastAPI()
https.configure(api)
api.include_router(
    emails_router, tags=["emails"], dependencies=[Depends(api_key_checker)]
)
