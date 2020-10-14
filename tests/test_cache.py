from datetime import timedelta
from typing import Any

from freezegun import freeze_time  # type: ignore
import pytest

from pycaches import Cache


def test_cache_saves_items() -> None:
    cache: Cache[Any, Any] = Cache()
    key, value = {"key"}, "value"

    assert not cache.has(key)
    with pytest.raises(KeyError):
        _ = cache.get(key)

    cache.save(key, value)

    assert cache.has(key)
    assert cache.get(key) == value


def test_cache_ignores_expired_items() -> None:
    cache: Cache[Any, Any] = Cache()
    key, value = {"key"}, "value"

    with freeze_time("2020-10-01 12:00:00"):
        cache.save(key, value, expire_in=timedelta(seconds=10))

    with freeze_time("2020-10-01 12:00:09"):
        assert cache.has(key)
        assert cache.get(key) == value

    with freeze_time("2020-10-01 12:00:10"):
        assert not cache.has(key)

        with pytest.raises(KeyError):
            _ = cache.get(key)
