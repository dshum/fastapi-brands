from aiocache import caches


def configure() -> None:
    caches.set_config({
        "default": {
            "cache": "aiocache.RedisCache",
            "endpoint": "127.0.0.1",
            "port": 6379,
            "timeout": 1,
            "serializer": {
                "class": "aiocache.serializers.PickleSerializer"
            },
            "plugins": [
                {"class": "aiocache.plugins.HitMissRatioPlugin"},
                {"class": "aiocache.plugins.TimingPlugin"}
            ]
        },
        "memory": {
            "cache": "aiocache.SimpleMemoryCache",
            "serializer": {
                "class": "aiocache.serializers.StringSerializer"
            }
        },
    })
