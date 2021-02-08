import pytest

from tests import AssertRequest, AssertResponse, assert_request
from cache import init_cache

ROUTE = "/fruit"

GET_INPUT = {
    "success": AssertRequest({}, {"name": "apple"}),
    "fail": AssertRequest({}, {"name": "banana"}),
}

GET_OUTPUT = {
    "success": AssertResponse({"name": "apple", "count": 1}, 200),
    "fail": AssertResponse("Bad Request", 400),
}


@pytest.mark.parametrize("test_type", GET_INPUT.keys())
def test_get(test_type):
    init_cache()
    assert_request("GET", ROUTE, GET_INPUT[test_type], GET_OUTPUT[test_type])


GET_URL_INPUT = {"success": "/apple", "fail": "/banana"}

GET_URL_OUTPUT = {
    "success": AssertResponse({"name": "apple", "count": 1}, 200),
    "fail": AssertResponse("Bad Request", 400),
}


@pytest.mark.parametrize("test_type", GET_URL_INPUT.keys())
def test_get_url(test_type):
    init_cache()
    assert_request(
        "GET",
        ROUTE + GET_URL_INPUT[test_type],
        AssertRequest({}, {}),
        GET_URL_OUTPUT[test_type],
    )


HEADERS = {"Content-Type": "Application/json"}

POST_INPUT = {
    "success": AssertRequest(HEADERS, {"name": "banana"}),
    "fail": AssertRequest(HEADERS, {"name": "apple"}),
}

POST_OUTPUT = {
    "success": AssertResponse("OK", 200),
    "fail": AssertResponse("Bad Request", 400),
}


@pytest.mark.parametrize("test_type", POST_INPUT.keys())
def test_post(test_type):
    init_cache()
    assert_request("POST", ROUTE, POST_INPUT[test_type], POST_OUTPUT[test_type])
