from typing import List

import pytest
from cache import REDIS
from models import Fruit


def clean_db():
    Fruit.query().delete()
    Fruit.commit()


def init_db():
    Fruit(**{"name": "apple", "count": 1}).add()
    Fruit.commit()


def init_cache():
    fruits: List[Fruit] = Fruit.query().all()
    for fruit in fruits:
        REDIS.set(fruit.name, f"{fruit.count}")
    # Intended to trigger server error
    REDIS.set("error", "error")


@pytest.fixture(autouse=True)
def preinit():
    """
    Pytest decorator to run preprcessing proceduce before each test case
    ex: init database and cache
    """
    clean_db()
    REDIS.flushdb()
    init_db()
    init_cache()
