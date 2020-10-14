"""
Dictionary-like collection
with restrictions on total size and storage time
and replacement of elements
"""


from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generic, Optional, TypeVar

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
    expire_at: Optional[datetime]

    def expired(self) -> bool:
        """
        Checks if item is expired
        """

        if self.expire_at is None:
            return False

        return datetime.now() >= self.expire_at


class Cache(Generic[Key, Value]):
    """
    Dictionary-like collection
    with restrictions on total size and storage time
    and replacement of elements
    """

    def __init__(self) -> None:
        self._map: Map[Key, CacheItem[Value]] = Map()

    def save(
        self,
        key: Key,
        value: Value,
        expire_in: Optional[timedelta] = None,
    ) -> None:
        """
        Adds item to cache
        """

        expire_at: Optional[datetime] = None
        if expire_in is not None:
            expire_at = datetime.now() + expire_in

        self._map[key] = CacheItem(value, expire_at)

    def has(self, key: Key) -> bool:
        """
        Checks if item with `key` is cached and not expired
        """

        return key in self._map and not self._map[key].expired()

    def get(self, key: Key) -> Value:
        """
        Returns cached item for `key`
        or raises `KeyError` if item is expired
        """

        item = self._map[key]
        if item.expired():
            raise KeyError(key)

        return item.value
