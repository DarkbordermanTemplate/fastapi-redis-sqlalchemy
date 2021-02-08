"""Routing table, gather route to main router for API"""
from typing import List
from endpoints.classes import Resource

from .health import HEALTH
from .fruit import FRUIT

RESOURCES: List[Resource] = HEALTH + FRUIT
