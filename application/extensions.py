from flask_caching import Cache
from minio import Minio
from minio.error import S3Error

cache = Cache()
storage = Minio("localhost:9000",
    access_key="root",
    secret_key="changeme",
    secure=False
)

storage.make_bucket("sensor-storage")