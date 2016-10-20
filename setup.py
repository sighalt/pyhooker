# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from setuptools import setup

__author__ = 'sighalt'


setup(
    name="pyhooker",
    version="1.0.1",
    author="Jakob Rößler",
    author_email="roessler@sighalt.de",
    description="Just another python DI library.",
    license="GPL3",
    url="https://github.com/sighalt/pyhooker",
    download_url="https://github.com/sighalt/pyhooker/tarball/1.0.1",
    packages=['pyhooker'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development",
    ],
    keywords=[
        "DI",
        "dependency injection",
        "inversion of control",
        "IOC",
    ],
    extras_require={
        "docs": ["sphinx"]
    }
)
