import redis
import os


def put_photos_to_redis():
    r = redis.Redis(host="localhost", port=63780, db=0)
    for filename in os.listdir("photos"):
        with open(os.path.join("photos", filename), "rb") as f:
            photo_bytes = f.read()
            r.lpush("photos", photo_bytes)
