![Logo](https://raw.githubusercontent.com/codingjerk/pycaches/master/assets/social.png)

[![PyPI](https://img.shields.io/pypi/v/pycaches?style=flat-square)](https://pypi.org/project/pycaches/)
[![Travis build on master](https://img.shields.io/travis/codingjerk/pycaches/master?style=flat-square)](https://travis-ci.org/github/codingjerk/pycaches)
[![Travis build on develop](https://img.shields.io/travis/codingjerk/pycaches/develop?label=develop&style=flat-square)](https://travis-ci.org/github/codingjerk/pycaches)
[![Codecov coverage](https://img.shields.io/codecov/c/gh/codingjerk/pycaches/develop?token=VHP5IBJTDJ&style=flat-square)](https://codecov.io/gh/codingjerk/pycaches/)
[![Chat on Gitter](https://img.shields.io/gitter/room/codingjerk/pycaches?style=flat-square)](https://gitter.im/codingjerk/pycaches)
![License](https://img.shields.io/pypi/l/pycaches?style=flat-square)

A bunch of caches.

## Features

✓ Ease of use `cache` decorator

✓ Support for non-`Hashable` keys (dictionaries, lists, sets)

✓ Different cache replacement policies (random, LRU)

✓ Time-based item expiration

□ Cache hit/miss statistics

□ Rich configuration, sane defaults

□ Optional persistency

## Installation

Recommended way is to use [poetry](https://python-poetry.org/):

```shell
poetry install pycaches
```

But you also can install library with pip:

```shell
pip install pycaches
```

## Usage

### `cache` decorator

```python
from pycaches import cache


@cache()
def example():
    print("Hi, I will be called once!")


example()  # Prints "Hi, I will be called once!"
example()  # Is not called
```

```python
import time

from pycaches import cache


@cache()
def long_computation(x):
    print("Performing long computation...")
    time.sleep(1)
    return x + 1


long_computation(5)  # Sleeps for 1 second and returns 6
long_computation(5)  # Immediately returns 6

long_computation(6)  # Sleeps for 1 second and returns 7
long_computation(6)  # Immediately returns 7
long_computation(6)  # And again
```

### `Cache` class

```python
import time
from datetime import timedelta

from pycaches import Cache


cache = Cache()
cache.save("a", 1)
cache.save("b", 2)
cache.save("c", 3, expire_in=timedelta(seconds=10))

cache.has("c")  # returns True
cache.get("a")  # returns 1

time.sleep(10)
cache.has("c")  # False
cache.get("c")  # raises KeyError
```

### Different cache replacement policies

```python
from pycaches import Cache
from pycaches.policies import LRU

"""
LRU stands for Least Recently Used.
So LRU policy removes Least Recently Used item from cache
if it's size exceed max_items.
"""


cache = Cache(max_items=2, replacement_policy=LRU())
cache.save("a", 1)
cache.save("b", 2)
cache.save("c", 3)

cache.has("a")  # returns False
cache.has("b")  # returns True

cache.save("d", 4)

cache.has("b")  # returns False
```

### Disable `deepcopy` for keys

```python
from pycaches import cache

"""
Cache class and cache decorator accepts `copy_keys` argument.
If you can garantee that keys will not change even if they are mutable,
you may set it to `True` to speed things up.
"""


@cache(copy_keys=False)
def faster_caching(x):
    return x


faster_caching({1, 2, 3})  # returns {1, 2, 3}
```

## Contribution

Just clone repository, make your changes and create a pull request.

Do not forget to make sure code quality is high: run linters, typecheckers, check code coverage, etc. You can do it all with `make`:

1. `make lint`: `pylint` and `pycodestyle`
1. `make typecheck`: `mypy`
1. `make test`: `pytest`
1. `make coverage`: `pytest` with `pytest-cov`
1. `make quality`: `radon`
1. `make build`: `setup.py`

And just `make` or `make all` to run all these targets.
