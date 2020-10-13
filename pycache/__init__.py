"""
A bunch of caches
"""

from typing import (
    Any, Dict, Generic, Hashable, Iterator, List,
    Mapping, MutableMapping, Tuple, TypeVar, Union
)
from dataclasses import dataclass


Key = TypeVar("Key")
Value = TypeVar("Value")


@dataclass
class KeyValue(Generic[Key, Value]):
    """
    Element of Map for unhashable keys
    """

    key: Key
    value: Value


class Map(MutableMapping[Key, Value]):
    """
    Dict-like collection with no `Hashable` restriction on elements
    """

    from_collection: Dict[Key, Value]

    def __init__(
        self,
        from_collection: Union[
            None,
            Mapping[Key, Value],
            List[Tuple[Key, Value]],
        ] = None,
    ) -> None:
        self.from_collection = dict(from_collection or [])

        self._unhashable_items: List[KeyValue[Key, Value]] = list()

    def copy(self) -> "Map[Key, Value]":
        """
        Returns shallow copy of Map
        """

        clone = Map(self.from_collection)

        for item in self._unhashable_items:
            clone[item.key] = item.value

        return clone

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Map) \
            and self.from_collection == other.from_collection \
            and self._unhashable_items == other._unhashable_items

    def __len__(self) -> int:
        return len(self.from_collection) + len(self._unhashable_items)

    def __getitem__(self, key: Key) -> Value:
        if not isinstance(key, Hashable):
            return self.__getitem_unhashable(key)

        return self.from_collection[key]

    def __contains__(self, key: Any) -> bool:
        if not isinstance(key, Hashable):
            return self.__contains_unhashable(key)

        return key in self.from_collection

    def __iter__(self) -> Iterator[Key]:
        for key in self.from_collection:
            yield key

        for item in self._unhashable_items:
            yield item.key

    def __setitem__(self, key: Key, value: Value) -> None:
        if not isinstance(key, Hashable):
            self.__setitem_unhashable(key, value)
            return

        self.from_collection[key] = value

    def __delitem__(self, key: Key) -> None:
        if not isinstance(key, Hashable):
            self.__delitem_unhashable(key)
            return

        del self.from_collection[key]

    def __getitem_unhashable(self, key: Key) -> Value:
        for item in self._unhashable_items:
            if item.key == key:
                return item.value

        raise KeyError(key)

    def __contains_unhashable(self, key: Key) -> bool:
        for item in self._unhashable_items:
            if item.key == key:
                return True

        return False

    def __setitem_unhashable(self, key: Key, value: Value) -> None:
        for item in self._unhashable_items:
            if item.key == key:
                item.value = value
                return

        self._unhashable_items.append(KeyValue(key, value))

    def __delitem_unhashable(self, key: Key) -> None:
        for item in self._unhashable_items:
            if item.key == key:
                return self._unhashable_items.remove(item)

        raise KeyError(key)
