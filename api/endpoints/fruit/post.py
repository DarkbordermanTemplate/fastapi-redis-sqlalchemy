from fastapi.responses import PlainTextResponse
from loguru import logger
# pylint: disable=E0611
from pydantic import BaseModel

from cache import REDIS

# pylint: enable=E0611

DOC = {
    200: {
        "description": "API response successfully",
        "content": {"application/json": {"example": {"name": "apple", "count": 0}}},
    }
}


class Payload(BaseModel):
    name: str
    count: int = 0


def post(payload: Payload):
    try:
        if REDIS.get(f"{payload.name}"):
            raise Exception(f"Fruit {payload.name} already exists!")
        REDIS.set(f"{payload.name}", f"{payload.count}")
        return PlainTextResponse("OK", 200)
    except Exception as error:
        logger.warning(error)
        return PlainTextResponse("Bad Request", 400)
