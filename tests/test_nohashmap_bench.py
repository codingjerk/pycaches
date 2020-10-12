import random

import pycache


def test_map_setitem_performance(benchmark) -> None:
    pycache_map = pycache.Map()
    def insert_pycache_map():
        value = random.random()

        for _ in range(100):
            key = random.randint(1, 75)
            pycache_map[{"key": key}] = value

    benchmark(insert_pycache_map)


def test_dict_setitem_performance(benchmark) -> None:
    dict_map = dict()
    def insert_dict_map():
        value = random.random()

        for _ in range(100):
            key = random.randint(1, 75)
            dict_map[("key", key)] = value

    benchmark(insert_dict_map)


def test_empty_map_contains_performance(benchmark) -> None:
    pycache_map = pycache.Map()
    def get_from_pycache_map():
        key = random.randint(1, 75)
        _ = {"key": key} in pycache_map

    benchmark(get_from_pycache_map)


def test_empty_dict_contains_performance(benchmark) -> None:
    dict_map = dict()
    def get_from_dict_map():
        key = random.randint(1, 75)
        _ = ("key", key) in dict_map

    benchmark(get_from_dict_map)
