#!/usr/bin/env python

"""Setup script for the pyparsing module distribution."""

# Setuptools depends on pyparsing (via packaging) as of version 34, so allow
# installing without it to avoid bootstrap problems.
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
import os

from pyparsing import __version__ as pyparsing_version
    
modules = ["pyparsing",]

setup(# Distribution meta-data
    name = "pyparsing",
    version = pyparsing_version,
    description = "Python parsing module",
    author = "Paul McGuire",
    author_email = "ptmcg@users.sourceforge.net",
    url = "http://pyparsing.wikispaces.com/",
    download_url = "http://sourceforge.net/project/showfiles.php?group_id=97203",
    license = "MIT License",
    py_modules = modules,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ]
    )
