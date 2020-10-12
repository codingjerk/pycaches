from typing import Any
import pytest

import pycache


def test_map_constructors() -> None:
    pycache_map: pycache.Map[str, int] = pycache.Map()
    assert len(pycache_map) == 0

    pycache_map = pycache.Map({"1": 1})
    assert pycache_map["1"] == 1

    pycache_map = pycache.Map([("2", 2)])
    assert pycache_map["2"] == 2


def test_map_to_dictionary() -> None:
    python_dict = {"1": 1, "2": 2, "3": 3}
    pycache_map = pycache.Map(python_dict)

    assert dict(pycache_map) == python_dict


def test_map_in_operator() -> None:
    pycache_map = pycache.Map({"1": 1, "2": 2, "3": 3})

    assert "1" in pycache_map
    assert "2" in pycache_map
    assert "3" in pycache_map
    assert "4" not in pycache_map
    assert None not in pycache_map


def test_map_getitem() -> None:
    pycache_map = pycache.Map({"1": 1, "2": 2, "3": 3})

    assert pycache_map["1"] == 1
    assert pycache_map["2"] == 2
    assert pycache_map["3"] == 3

    with pytest.raises(KeyError):
        _ = pycache_map["4"]


def test_map_len() -> None:
    pycache_map = pycache.Map({"1": 1, "2": 2, "3": 3})
    assert len(pycache_map) == 3

    pycache_map["4"] = 4
    assert len(pycache_map) == 4

    pycache_map["1"] = 11
    assert len(pycache_map) == 4


def test_map_setitem() -> None:
    pycache_map = pycache.Map({"1": 1, "2": 2, "3": 3})
    pycache_map["1"] = 11
    pycache_map["4"] = 4

    assert pycache_map["1"] == 11
    assert pycache_map["4"] == 4


def test_map_delitem() -> None:
    pycache_map = pycache.Map({"1": 1, "2": 2, "3": 3})
    del pycache_map["1"]

    assert "1" not in pycache_map


def test_unhashable_items_in_maps() -> None:
    pycache_map: pycache.Map[Any, str] = pycache.Map()
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
    pycache_map: pycache.Map[Any, str] = pycache.Map()
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
    pycache_map: pycache.Map[Any, str] = pycache.Map()

    with pytest.raises(KeyError):
        _ = pycache_map[["not existed value"]]

    with pytest.raises(KeyError):
        del pycache_map[["not existed value"]]
