"""Routing table, gather route to main router for API"""
from typing import List

from endpoints.classes import Resource

from .fruit import FRUIT
from .health import HEALTH

RESOURCES: List[Resource] = HEALTH + FRUIT
