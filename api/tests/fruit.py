import pytest
from tests import APITestcase, AssertRequest, AssertResponse

ROUTE = "/fruit"

HEADERS = {"Content-Type": "Application/json"}

CASES = [
    APITestcase(
        "ok",
        AssertRequest("GET", ROUTE, {}, {"name": "apple"}),
        AssertResponse({"name": "apple", "count": 1}, 200),
    ),
    APITestcase(
        "bad_request",
        AssertRequest("GET", ROUTE, {}, {"name": "banana"}),
        AssertResponse("Bad Request", 400),
    ),
    APITestcase(
        "internal_server_error",
        AssertRequest("GET", ROUTE, {}, {"name": "error"}),
        AssertResponse("Internal Server Error", 500),
    ),
    APITestcase(
        "ok",
        AssertRequest("POST", ROUTE, HEADERS, None, {"name": "banana"}),
        AssertResponse("OK", 200),
    ),
    APITestcase(
        "fail",
        AssertRequest("POST", ROUTE, HEADERS, None, {"name": "apple"}),
        AssertResponse("Bad Request", 400),
    ),
]


@pytest.mark.parametrize("case", CASES, ids=[case.name for case in CASES])
def test(case: APITestcase):
    case.run()
