from typing import Any

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
