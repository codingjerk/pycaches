# pycaches

[![PyPI](https://img.shields.io/pypi/v/pycaches?style=flat-square)](https://pypi.org/project/pycaches/)
[![Travis build on master](https://img.shields.io/travis/codingjerk/pycaches/master?style=flat-square)](https://travis-ci.org/github/codingjerk/pycaches)
[![Travis build on develop](https://img.shields.io/travis/codingjerk/pycaches/develop?label=develop&style=flat-square)](https://travis-ci.org/github/codingjerk/pycaches)
[![Codecov coverage](https://img.shields.io/codecov/c/gh/codingjerk/pycaches/develop?token=VHP5IBJTDJ&style=flat-square)](https://codecov.io/gh/codingjerk/pycaches/)
[![Chat on Gitter](https://img.shields.io/gitter/room/codingjerk/pycaches?style=flat-square)](https://gitter.im/codingjerk/pycaches)
![License](https://img.shields.io/pypi/l/pycaches?style=flat-square)

A bunch of caches

## Installation

`$ pip install pycaches`

## Usage

### Decorator

```
from pycaches import cache


@cache()
def example():
    print("Hi, I will be called once!")

example()  # Prints "Hi, I will be called once!"
example()  # Is not called
```

```
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

## Contribution

Just clone repository, make your changes and create a pull request.

Do not forget to make sure code quality is high: run linters, typecheckers, check code coverage, etc. You can do it all with `make`:

1. `make lint`: `pylint` and `pycodestyle`
1. `make typecheck`: `mypy`
1. `make test`: `pytest`
1. `make coverage`: `pytest` with `pytest-cov`
1. `make quality`: `radon`
1. `make build`: `setup.py`

And just `make` or `make all` to run all these targets
