from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Resource:
    """Default resource for route"""

    method: str
    route: str
    endpoint: Callable
    description: str = "None"
    summary: str = "None"
    doc: dict = field(default_factory=dict)
