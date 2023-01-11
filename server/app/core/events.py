from typing import Callable

from fastapi import FastAPI


def create_startup_handler(app: FastAPI) -> Callable: # type: ignore
    async def start_app() -> None:
     