from redis import StrictRedis

from config import Config

REDIS: StrictRedis = StrictRedis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=Config.REDIS_DB_IDX,
    password=Config.REDIS_PASSWORD,
)


def init_cache():
    REDIS.set("apple", f"{1}")
