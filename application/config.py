import os

FLASK_PORT = os.environ.get("FLASK_PORT", 5000)

CACHE_TYPE = os.environ.get("CACHE_TYPE", "RedisCache")
CACHE_REDIS_HOST = os.environ.get("CACHE_REDIS_HOST", "localhost")
CACHE_REDIS_PORT = os.environ.get("CACHE_REDIS_PORT", 6379)
CACHE_REDIS_DB = os.environ.get("CACHE_REDIS_DB", 0)