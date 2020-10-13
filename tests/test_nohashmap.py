from typing import Any
import pytest

from pycache import Map


def test_map_constructors() -> None:
    pycache_map: Map[str, int] = Map()
    assert len(pycache_map) == 0

    pycache_map = Map({"1": 1})
    assert pycache_map["1"] == 1

    pycache_map = Map([("2", 2)])
    assert pycache_map["2"] == 2


def test_map_to_dictionary() -> None:
    python_dict = {"1": 1, "2": 2, "3": 3}
    pycache_map = Map(python_dict)

    assert dict(pycache_map) == python_dict


def test_map_in_operator() -> None:
    pycache_map = Map({"1": 1, "2": 2, "3": 3})

    assert "1" in pycache_map
    assert "2" in pycache_map
    assert "3" in pycache_map
    assert "4" not in pycache_map
    assert None not in pycache_map


def test_map_getitem() -> None:
    pycache_map = Map({"1": 1, "2": 2, "3": 3})

    assert pycache_map["1"] == 1
    assert pycache_map["2"] == 2
    assert pycache_map["3"] == 3

    with pytest.raises(KeyError):
        _ = pycache_map["4"]


def test_map_len() -> None:
    pycache_map = Map({"1": 1, "2": 2, "3": 3})
    assert len(pycache_map) == 3

    pycache_map["4"] = 4
    assert len(pycache_map) == 4

    pycache_map["1"] = 11
    assert len(pycache_map) == 4


def test_map_setitem() -> None:
    pycache_map = Map({"1": 1, "2": 2, "3": 3})
    pycache_map["1"] = 11
    pycache_map["4"] = 4

    assert pycache_map["1"] == 11
    assert pycache_map["4"] == 4


def test_map_delitem() -> None:
    pycache_map = Map({"1": 1, "2": 2, "3": 3})
    del pycache_map["1"]

    assert "1" not in pycache_map


def test_unhashable_items_in_maps() -> None:
    pycache_map: Map[Any, str] = Map()
    examples = [
        (["key"], "list value"),
        ({"key": "key"}, "dict value"),
        ({"key"}, "set value"),
    ]

    for key, value in examples:
        pycache_map[key] = value
        assert pycache_map[key] == value
        assert key in pycache_map

    assert len(pycache_map) == len(examples)

    pycache_map[examples[0][0]] = "any value"
    assert len(pycache_map) == len(examples)


def test_unhashable_items_deletion() -> None:
    pycache_map: Map[Any, str] = Map()
    examples = [
        (["key"], "list value"),
        ({"key": "key"}, "dict value"),
        ({"key"}, "set value"),
    ]
    for key, value in examples:
        pycache_map[key] = value

    for key, _ in examples:
        del pycache_map[key]
        assert key not in pycache_map


def test_unhashable_items_raises_errors() -> None:
    pycache_map: Map[Any, str] = Map()

    with pytest.raises(KeyError):
        _ = pycache_map[["not existed value"]]

    with pytest.raises(KeyError):
        del pycache_map[["not existed value"]]


def test_map_keys_values_items() -> None:
    pycache_map: Map[Any, int] = Map({"1": 1})
    pycache_map[{"2"}] = 2

    assert list(pycache_map.keys()) == ["1", {"2"}]
    assert list(pycache_map.values()) == [1, 2]
    assert list(pycache_map.items()) == [("1", 1), ({"2"}, 2)]


def test_map_get() -> None:
    pycache_map: Map[Any, int] = Map({"1": 1})
    pycache_map[{"2"}] = 2

    assert pycache_map.get({"2"}) == 2
    assert pycache_map.get({"3"}) is None
    assert pycache_map.get({"4"}, 4) == 4


def test_map_setdefault() -> None:
    pycache_map: Map[Any, int] = Map({"1": 1})
    pycache_map[{"2"}] = 2

    pycache_map.setdefault({"3"}, 3)
    assert pycache_map.get({"3"}) == 3


def test_map_pop() -> None:
    pycache_map: Map[Any, int] = Map({"1": 1})
    pycache_map[{"2"}] = 2

    assert len(pycache_map) == 2
    assert pycache_map.pop({"2"}) == 2
    assert len(pycache_map) == 1


def test_map_update() -> None:
    pycache_map: Map[Any, int] = Map({"1": 1})
    pycache_map[{"2"}] = 2

    pycache_map.update([
        ("1", 11),
        ({"2"}, 22),
    ])
    assert pycache_map["1"] == 11
    assert pycache_map[{"2"}] == 22


def test_map_clear() -> None:
    pycache_map: Map[Any, int] = Map({"1": 1})
    pycache_map[{"2"}] = 2

    pycache_map.clear()
    assert len(pycache_map) == 0


def test_map_copy() -> None:
    pycache_map: Map[Any, int] = Map({"1": 1})
    pycache_map[{"2"}] = 2

    newmap = pycache_map.copy()
    assert newmap == pycache_map
    assert id(newmap) != id(pycache_map)


def test_map_equality() -> None:
    assert Map({"1": 1, "2": 2}) == Map({"2": 2, "1": 1})
    assert Map({"1": 1, "2": 2}) != Map({"2": 2})
    assert Map({"1": 1, "2": 2}) != Map({"3": 3, "2": 2, "1": 1})

    assert Map({"1": 1, "2": 2}) != [1, 2]
    assert Map({"1": 1, "2": 2}) != {"1": 1, "2": 2}


def test_map_iterable() -> None:
    pycache_map: Map[Any, int] = Map({"1": 1, "2": 2, "3": 3})
    pycache_map[{4: 4}] = 4

    keys = [key for key in pycache_map]  # pylint: disable=R1721
    assert keys == ["1", "2", "3", {4: 4}]
