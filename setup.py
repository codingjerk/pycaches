#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="pycaches",
    packages=find_packages(include="pycaches"),
    version="0.0.1",
    description="A bunch of caches",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/codingjerk/pycaches",
    author="Denis Gruzdev",
    author_email="codingjerk@gmail.com",
    license="MIT",

    install_requires=[
    ],
    setup_requires=[
    ],
    tests_require=[
        "mypy==0.782",
        "pycodestyle==2.6.0",
        "pylint==2.6.0",
        "pytest-benchmark==3.2.3",
        "pytest-cov==2.10.1",
        "pytest-runner==5.2",
        "pytest==6.0.1",
        "radon==4.3.2",
    ],
    test_suite="tests",
)
