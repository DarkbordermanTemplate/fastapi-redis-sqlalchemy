"""Testing module"""
from dataclasses import dataclass
from typing import Any, Union

from fastapi.testclient import TestClient

from app import APP


CLIENT = TestClient(APP)


@dataclass
class AssertRequest:
    """
    API request assertion dataclass

    headers (Union[dict, None]): The expected headers of request
    payload (Union[dict, None]): The expceted payload(json or GET parameters) of request
    """

    headers: Union[dict, None]
    payload: Union[dict, None]


@dataclass
class AssertResponse:
    """
    API response assertion dataclass

    body (Any): The expected body of response
    status_code (int): The expected status code of response
    """

    body: Any = "OK"
    status_code: int = 200


def assert_request(
    method: str, route: str, request: AssertRequest, response: AssertResponse
):
    if method.upper() == "GET":
        resp = CLIENT.request(
            method,
            f"{route}",
            headers=request.headers,
            params=request.payload,
        )
    else:
        resp = CLIENT.request(
            method,
            f"{route}",
            headers=request.headers,
            json=request.payload,
        )

    try:
        assert (
            resp.json() == response.body
        ), f"{resp.json} does not match {response.body}"
    except Exception:
        assert resp.text == response.body, f"{resp.body} does not match {response.body}"

    assert (
        resp.status_code == response.status_code
    ), f"{resp.status_code} does not match {response.status_code}"
