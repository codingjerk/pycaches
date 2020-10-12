"""
A bunch of caches
"""

from typing import Any, Dict, Generic, Hashable, Iterator, List, Mapping, MutableMapping, Tuple, TypeVar, Union


Key = TypeVar("Key")
Value = TypeVar("Value")


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

        self.__unhashable_items: List[List[Union[Key, Value]]] = list()

    def __len__(self) -> int:
        return len(self.from_collection) + len(self.__unhashable_items)

    def __getitem__(self, key: Key) -> Value:
        if not isinstance(key, Hashable):
            return self.__getitem_unhashable(key)

        return self.from_collection[key]

    def __contains__(self, key: Any) -> bool:
        if not isinstance(key, Hashable):
            return self.__contains_unhashable(key)

        return key in self.from_collection

    def __iter__(self) -> Iterator[Key]:
        return iter(self.from_collection)

    def __setitem__(self, key: Key, value: Value) -> None:
        if not isinstance(key, Hashable):
            return self.__setitem_unhashable(key, value)

        self.from_collection[key] = value

    def __delitem__(self, key: Key) -> None:
        if not isinstance(key, Hashable):
            return self.__delitem_unhashable(key)

        del self.from_collection[key]

    def __getitem_unhashable(self, key: Key) -> Value:
        for item in self.__unhashable_items:
            if item[0] == key:
                return item[1]

        raise KeyError(key)

    def __contains_unhashable(self, key: Key) -> bool:
        for item in self.__unhashable_items:
            if item[0] == key:
                return True

        return False

    def __setitem_unhashable(self, key: Key, value: Value) -> None:
        for item in self.__unhashable_items:
            if item[0] == key:
                item[1] = value
                break

        self.__unhashable_items.append([key, value])

    def __delitem_unhashable(self, key: Key) -> None:
        for item in self.__unhashable_items:
            if item[0] == key:
                return self.__unhashable_items.remove(item)

        raise KeyError(key)
