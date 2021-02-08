from cache import REDIS
from common.enums import EnumResponse
from fastapi.responses import JSONResponse
from loguru import logger

DOC = {
    200: {
        "description": "API response successfully",
        "content": {"application/json": {"example": {"name": "apple"}}},
    },
    400: EnumResponse.BAD_REQUEST.value.doc,
    500: EnumResponse.INTERNAL_SERVER_ERROR.value.doc,
}


def get(name: str):
    try:
        if REDIS.get(name) is None:
            return EnumResponse.BAD_REQUEST.value.response
        return JSONResponse({"name": name, "count": int(REDIS.get(name).decode())}, 200)  # type: ignore
    except Exception as error:
        logger.warning(error)
        return EnumResponse.INTERNAL_SERVER_ERROR.value.response
