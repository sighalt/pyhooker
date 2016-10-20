# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup

__author__ = 'sighalt'


setup(
    name="pyhooker",
    version="1.0.0",
    author="Jakob Rößler",
    author_email="roessler@sighalt.de",
    description="Just another python DI library.",
    license="GPL3",
    keywords="DI dependency injection inversion of control container IOC",
    url="https://github.com/sighalt/pyhooker",
    packages=['pyhooker'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    extras_require={
        "docs": ["sphinx"]
    }
)
