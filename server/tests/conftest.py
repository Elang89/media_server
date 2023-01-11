import pytest
import pytest_asyncio
import docker as libdocker


from mimesis.random import Random
from mimesis import Internet
from os import environ, getenv
from fastapi import FastAPI
from asgi_lifespan import LifespanManager
from httpx import AsyncClient


MONGO_DOCKER_IMAGE = "mongo:4.2.23"
MONGO_DOCKER_CONTAINER_NAME = "test-mongo"

USE_LOCAL_DB = getenv("USE_LOCAL_DB_FOR_TEST", False)

pytest_plugins = ["tests.common.fixtures_stream"]

@pytest.fixture
def docker() -> libdocker.APIClient:
    with libdocker.APICLient(version="auto") as client:
        yield client


@pytest.fixture
def app() -> FastAPI:
    from main import get_application

    return get_application()

@pytest_asyncio.fixture
async def initialized_app(app: FastAPI):
    async with LifespanManager(app):
        yield app


@pytest_asyncio.fixture
async def client(initialized_app: FastAPI):
    async with AsyncClient(
        app=initialized_app,
        base_url="http://testserver",
        headers={"Content-Type": "application/json"},
    ) as client:
        yield client


@pytest.fixture
def random_generator() -> Random:
    return Random()


@pytest.fixture
def internet() -> Internet:
    return Internet()