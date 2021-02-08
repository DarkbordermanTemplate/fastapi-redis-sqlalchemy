from endpoints.classes import Resource

from .get import DOC as get_doc
from .get import get

HEALTH = [
    Resource("GET", "/health", get, "Used for health check", "Health check", get_doc)
]
