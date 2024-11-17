#!/usr/bin/env python
# -*- mode: python ; coding: utf-8 -*-

import re
#from setuptools import setup, find_packages
from setuptools import *

#with open("idx.rst", "r", encoding="utf-8") as f:
    #long_description = f.read()

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('mkgtree/mkgtree.py').read(),
    re.M
    ).group(1)

setup(
    name='givtrae',
    packages=["mkgtree"],
    entry_points = {
        "console_scripts": ["givtrae = mkgtree.mkgtree:main"]
    },
    version=version,
    description='A simple tool for quickly generating a file tree in the selected directory.',
    long_description="",
    url="https://github.com/AquaQuokka/givtrae",
    author="AquaQuokka",
    license='BSD-3-Clause',
    py_modules=['mkgtree'],
    scripts=['mkgtree/mkgtree.py']
)
