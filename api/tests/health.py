import pytest
from tests import APITestcase, AssertRequest, AssertResponse

ROUTE = "/health"

CASES = [
    APITestcase(
        "ok", AssertRequest("GET", ROUTE, None, None), AssertResponse("OK", 200)
    )
]


@pytest.mark.parametrize("case", CASES, ids=[case.name for case in CASES])
def test(case: APITestcase):
    case.run()
