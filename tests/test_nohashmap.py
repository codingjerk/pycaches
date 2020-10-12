import pytest
import pycache


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
