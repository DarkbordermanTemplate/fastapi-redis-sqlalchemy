from dataclasses import dataclass
from typing import Union

from app import APP
from fastapi.testclient import TestClient

CLIENT = TestClient(APP)


@dataclass
class AssertRequest:
    """
    API request assertion class

    Attributes:
        method (str): HTTP method of request
        url (str): HTTP url of request
        headers (Union[dict, None]): Headers of request
        params (Union[dict, None]): Parameters of request (for GET)
        json (Union[dict, None]): JSON payload of request (for POST, PUT, DELETE)
    """

    method: str
    url: str
    headers: Union[dict, None] = None
    params: Union[dict, None] = None
    json: Union[dict, None] = None


@dataclass
class AssertResponse:
    """
    API response assertion class

    Attributes:
        body (Union[dict, str]): The expected body of response
        status_code (int): The expected status code of response
    """

    body: Union[dict, str]
    status_code: int


@dataclass
class APITestcase:
    """
    API testcase assertion class

    Attributes:
        name (str): Test case's name
        request (AssertRequest): Asserted Request
        response (AssertResponse): Asserted Response
    """

    name: str
    request: AssertRequest
    response: AssertResponse

    def run(self):
        resp = CLIENT.request(
            self.request.method,
            self.request.url,
            headers=self.request.headers,
            params=self.request.params,
            json=self.request.json,
        )
        if isinstance(self.response.body, str):
            assert (
                resp.text == self.response.body
            ), f"{resp.text} does not match {self.response.body}"
        else:
            assert (
                resp.json() == self.response.body
            ), f"{resp.json} does not match {self.response.body}"
        assert (
            resp.status_code == self.response.status_code
        ), f"{resp.status_code} does not match {self.response.status_code}"
