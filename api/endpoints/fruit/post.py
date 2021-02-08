from cache import REDIS
from common.enums import EnumResponse
from loguru import logger
from models import Fruit

# pylint: disable=E0611
from pydantic import BaseModel

# pylint: enable=E0611

DOC = {200: EnumResponse.OK.value.doc, 400: EnumResponse.BAD_REQUEST.value.doc}


class Payload(BaseModel):
    name: str
    count: int = 0


def post(payload: Payload):
    try:
        if REDIS.get(f"{payload.name}"):
            raise Exception(f"Fruit {payload.name} already exists!")
        Fruit(**{"name": payload.name, "count": payload.count}).add()
        Fruit.commit()
        REDIS.set(f"{payload.name}", f"{payload.count}")
        return EnumResponse.OK.value.response
    except Exception as error:
        logger.warning(error)
        return EnumResponse.BAD_REQUEST.value.response
