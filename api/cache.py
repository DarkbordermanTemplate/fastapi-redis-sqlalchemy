from typing import List

from redis import StrictRedis

from config import Config
from db import SESSION
from model import Fruit

REDIS: StrictRedis = StrictRedis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=Config.REDIS_DB_IDX,
    password=Config.REDIS_PASSWORD,
)


def init_cache():
    fruits: List[Fruit] = SESSION.query(Fruit).all()
    for fruit in fruits:
        REDIS.set(fruit.name, f"{fruit.count}")
