import os

FLASK_HOST = os.environ.get("FLASK_HOST", "0.0.0.0")
FLASK_PORT = os.environ.get("FLASK_PORT", 5000)
CACHE_TYPE = "RedisCache"
CACHE_REDIS_HOST = "localhost"
CACHE_REDIS_PORT = "6379"
CACHE_REDIS_DB = 0