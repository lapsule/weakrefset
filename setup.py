#! /usr/bin/env python
# setup.py
# Copyright (C) 2010 Michael Foord
# E-mail: fuzzyman AT voidspace DOT org DOT uk

# This software is licensed under the terms of the BSD license.
# http://www.voidspace.org.uk/python/license.shtml

import os
import sys
from distutils.core import setup
from weakrefset import __version__ as VERSION

NAME = 'weakrefset'

MODULES = ['weakrefset']

DESCRIPTION = 'A WeakSet class for storing objects using weak references.'

URL = 'http://pypi.python.org/pypi/weakrefset'

LONG_DESCRIPTION = """
Python 2.7 & 3.1 include a ``WeakSet`` class, a collection for storing objects using weak references 
(see the `Python weakref module <http://docs.python.org/library/weakref.html>`_).

This project is a backport of the weakrefset module, and tests, for Python 2.5 and 2.6. The tests 
require the `unittest2 package <http://pypi.python.org/pypi/unittest2>`_. 

* Mercurial repository & issue tracker: http://code.google.com/p/weakrefset/

You can install it with: ``pip install weakrefset``

Usage is straightforward. You don't need to deal with weak references themselves, the WeakSet manages 
the references and you can add / remove / iterate over your objects directly::

    >>> from weakrefset import WeakSet
    >>> class Foo(object): pass
    ...
    >>> f1 = Foo()
    >>> f2 = Foo()
    >>> refs = WeakSet([f1, f2])
    >>> f3 = Foo()
    >>> refs.add(f3)
    >>> refs.remove(f1)
    >>> del f2
    >>> f3 in refs
    True
    >>> for f in refs:
    ...  print f
    ...
    <__main__.Foo object at 0x40e410>

To be compatible with Python 2.5, 2.6 and future versions of Python you can import it like this::

    try:
        # location in Python 2.7 and 3.1
        from weakref import WeakSet
    except ImportError:
        # separately installed
        from weakrefset import WeakSet

"""[1:]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

AUTHOR = 'Michael Foord'

AUTHOR_EMAIL = 'michael@voidspace.org.uk'

KEYWORDS = "weakref set collection".split(', ')


setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
#      download_url=DOWNLOAD_URL,,
      py_modules=MODULES,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS
     )
