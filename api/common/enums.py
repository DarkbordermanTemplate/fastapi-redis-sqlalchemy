from dataclasses import dataclass
from enum import Enum

from fastapi.responses import PlainTextResponse


@dataclass
class DefaultResponse:
    doc: dict
    response: PlainTextResponse


class EnumResponse(Enum):
    OK = DefaultResponse(
        {"description": "OK", "content": {"text/plain": {"example": "OK"}}},
        PlainTextResponse("OK", 200),
    )

    BAD_REQUEST = DefaultResponse(
        {
            "description": "Bad Request",
            "content": {"text/plain": {"example": "Bad Request"}},
        },
        PlainTextResponse("Bad Request", 400),
    )

    UNAUTHORIZED = DefaultResponse(
        {
            "description": "Unauthorized",
            "content": {"text/plain": {"example": "Unauthorized"}},
        },
        PlainTextResponse("Unauthorized", 401),
    )

    NOT_FOUND = DefaultResponse(
        {
            "description": "Not Found",
            "content": {"text/plain": {"example": "Not Found"}},
        },
        PlainTextResponse("Not Found", 404),
    )

    INTERNAL_SERVER_ERROR = DefaultResponse(
        {
            "description": "Internal Server Error",
            "content": {"text/plain": {"example": "Internal Server Error"}},
        },
        PlainTextResponse("Internal Server Error", 500),
    )
