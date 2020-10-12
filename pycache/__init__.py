"""
A bunch of caches
"""

from typing import Any, Iterator, Generic, Mapping, MutableMapping, TypeVar


Key = TypeVar("Key")
Value = TypeVar("Value")


class Map(MutableMapping[Key, Value]):
    """
    Dict-like collection with no `Hashable` restriction on elements
    """

    def __init__(self, from_collection: MutableMapping[Key, Value]) -> None:
        self.from_collection = from_collection

    def __len__(self) -> int:
        return len(self.from_collection)

    def __getitem__(self, key: Key) -> Value:
        return self.from_collection[key]

    def __contains__(self, key: Any) -> bool:
        return key in self.from_collection

    def __iter__(self) -> Iterator[Key]:
        return iter(self.from_collection)

    def __setitem__(self, key: Key, value: Value) -> None:
        self.from_collection[key] = value

    def __delitem__(self, key: Key) -> None:
        del self.from_collection[key]
