# pycaches

[![PyPI](https://img.shields.io/pypi/v/pycaches?style=flat-square)](https://pypi.org/project/pycaches/)
[![Travis build on master](https://img.shields.io/travis/codingjerk/pycaches/master?style=flat-square)](https://travis-ci.org/github/codingjerk/pycaches)
[![Travis build on develop](https://img.shields.io/travis/codingjerk/pycaches/develop?label=develop&style=flat-square)](https://travis-ci.org/github/codingjerk/pycaches/develop)
[![Codecov coverage](https://img.shields.io/codecov/c/gh/codingjerk/pycaches/develop?token=VHP5IBJTDJ&style=flat-square)](https://codecov.io/gh/codingjerk/pycaches/)
[![Chat on Gitter](https://img.shields.io/gitter/room/codingjerk/pycaches?style=flat-square)](https://gitter.im/codingjerk/pycaches)
![License](https://img.shields.io/pypi/l/pycaches?style=flat-square)

A bunch of caches

## Installation

`$ pip install pycaches`

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
