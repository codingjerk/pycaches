all: typecheck test coverage lint quality build

.PHONY: test lint typecheck coverage quality benchmark build deploy test_deploy watch all

package = pycaches

test:
	@echo [ === TEST === ]
	@poetry run pytest --quiet --benchmark-disable --no-cov

lint:
	@echo [ === LINT === ]
	@poetry run pycodestyle $(package)
	@poetry run pylint --score=no --disable=W1116 $(package)
	@poetry run pycodestyle tests
	@poetry run pylint --score=no --disable=C0114,C0116,E0401,W0611,E1101 tests

typecheck:
	@echo [ === TYPECHECK === ]
	@poetry run mypy --strict --pretty --no-error-summary $(package)
	@poetry run mypy --strict --pretty --no-error-summary --allow-untyped-decorators tests

coverage:
	@echo [ === COVERAGE === ]
	@poetry run pytest --cov=$(package) --cov-branch --cov-fail-under=100 --cov-report=term-missing:skip-covered --benchmark-disable --quiet

quality:
	@echo [ === QUALITY === ]
	@! poetry run radon mi $(package)/**.py | grep -v " - A"
	@! poetry run radon cc $(package)/**.py | grep -vP "\.py"$ | grep -v " - A"

benchmark:
	@echo [ === BENCHMARK === ]
	@poetry run pytest --quiet --benchmark-only --benchmark-save=benchmark --no-cov

benchmark_compare:
	@echo [ === BENCHMARK === ]
	@poetry run pytest --quiet --benchmark-only --benchmark-compare --no-cov

build:
	@echo [ === BUILD === ]
	@poetry build

deploy:
	@echo [ === DEPLOY === ]
	@poetry publish --username "__token__" --password "${PYCACHES_DEPLOY}"

test_deploy:
	@echo [ === TEST DEPLOY === ]
	@sh tests/functional/test_deploy.sh

watch:
	@echo [ === WATCH === ]
	@while true; do \
		make --silent; \
		echo [ === WAITING FOR CHANGES === ]; \
		inotifywait -qqre close_write .; \
	done
