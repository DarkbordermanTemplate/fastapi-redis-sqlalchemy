from endpoints.classes import Resource

from .get import DOC as get_doc
from .get import get
from .get_url import DOC as get_url_doc
from .get_url import get_url
from .post import DOC as post_doc
from .post import post

FRUIT = [
    Resource(
        "GET",
        "/fruit",
        get,
        "Example route for GET request with header and query parmeters",
        "GET by query params",
        get_doc,
    ),
    Resource(
        "GET",
        "/fruit/{name}",
        get_url,
        "Example route for GET request with url parmeters",
        "GET by url params",
        get_url_doc,
    ),
    Resource(
        "POST",
        "/fruit",
        post,
        "Example route for POST request with JSON payload",
        "POST by JSON",
        post_doc,
    ),
]
