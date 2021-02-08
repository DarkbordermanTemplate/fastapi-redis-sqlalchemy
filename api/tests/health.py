import pytest

from tests import AssertRequest, AssertResponse, assert_request

ROUTE = "/health"

HEADERS = {}

PAYLOAD = {}

INPUT = {"success": AssertRequest(HEADERS, PAYLOAD)}

OUTPUT = {"success": AssertResponse("OK", 200)}


@pytest.mark.parametrize("test_type", INPUT.keys())
def test_get(test_type):
    assert_request("GET", ROUTE, INPUT[test_type], OUTPUT[test_type])
