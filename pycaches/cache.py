"""
Dictionary-like collection
with restrictions on total size and storage time
and replacement of elements
"""


from dataclasses import dataclass
from typing import Generic, TypeVar

from pycaches.nohashmap import Map


Key = TypeVar("Key")
Value = TypeVar("Value")


@dataclass
class CacheItem(Generic[Value]):
    """
    Cache item, containing value and metadata, such as:
    cache hits, last access time, expiration time, etc
    """

    value: Value


class Cache(Generic[Key, Value]):
    """
    Dictionary-like collection
    with restrictions on total size and storage time
    and replacement of elements
    """

    def __init__(self) -> None:
        self._map: Map[Key, CacheItem[Value]] = Map()

    def save(self, key: Key, value: Value) -> None:
        """
        Adds item to cache
        """

        self._map[key] = CacheItem(value)

    def has(self, key: Key) -> bool:
        """
        Checks if item with `key` is cached and not expired
        """

        return key in self._map

    def get(self, key: Key) -> Value:
        """
        Returns cached item for `key`
        or raises `KeyError` if item is expired
        """

        item = self._map[key]
        return item.value
