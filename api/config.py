import os


class Config:
    """Service configurations"""
    APP_TITLE = os.environ.get('APP_TITLE', 'FastAPI template')
    APP_DESCRIPTION = os.environ.get('APP_DESCRIPTION', 'A template for FastAPI.')
    VERSION = os.environ.get('VERSION', '0.0.0')
    OPENAPI_URL = os.environ.get("OPENAPI_URL", "/openapi.json")

    # Cache configuration
    REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
    REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))
    REDIS_DB_IDX = int(os.environ.get("REDIS_DB_IDX", "0"))
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "password")

    # Database configuration
    DB_URL = os.environ.get(
        'DB_URL', 'postgresql://postgres:password@localhost:5432/database'
    )
