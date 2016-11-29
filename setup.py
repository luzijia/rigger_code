#!/usr/bin/python

# -*- coding: UTF-8 -*-

import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

def read(fname):
   return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

NAME = "rigger_code"

PACKAGES = ["rigger_code","rigger_code.pymysql.constants","rigger_code.pymysql"]

DESCRIPTION = "this is a rigger for speeding up code."

LONG_DESCRIPTION = read("README.txt")

KEYWORDS = "test python package"

AUTHOR = "luzijia"

AUTHOR_EMAIL = "luzijia@email.com"

URL = "http://luzijia.net"

VERSION = "0.1"

LICENSE = "MIT"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)

