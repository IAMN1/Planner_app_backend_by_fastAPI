from beanie import init_beanie
import httpx
import pytest_asyncio

#from database.connection import Settings
from models.events import Event
from models.users import User
from motor.motor_asyncio import AsyncIOMotorClient

from fastapi import FastAPI
from routes.events import event_router
from routes.users import user_router

app_for_tests = FastAPI()
app_for_tests.include_router(user_router, prefix="/user")
app_for_tests.include_router(event_router, prefix='/event')

@pytest_asyncio.fixture(scope="function")
async def default_client():
    client = AsyncIOMotorClient("mongodb://localhost:27017/testdb")

    await init_beanie(
        database=client.get_default_database(),
        document_models=[Event, User],
        allow_index_dropping=True
    )

    transport = httpx.ASGITransport(app=app_for_tests)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as http_client:
        yield http_client

        await Event.find_all().delete()
        await User.find_all().delete()