#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#   pyasa - python bindings for Adaptive Simulated Annealing
#   Copyright (C) 2012 Robert Jordens <jordens@gmail.com>
#   Modified by Cole Lyman <cole@colelyman.com>

try:
    from setuptools import setup, Extension
except ImportError:
    from distutils import setup
    from distutils.extension import Extension

from Cython.Distutils import build_ext
import numpy
import os

setup(
    name="pyasa",
    description="Adaptive Simulated Annealing",
    long_description= """Python bindings for the ASA code from
    http://www.ingber.com/#ASA""",
    version="0.5+dev",
    author="Robert Jordens",
    author_email="jordens@gmail.com",
    url="https://github.com/jordens/pyasa",
    license="modified BSD",
    install_requires=["numpy"],
    #packages=["asa"],
    cmdclass = {"build_ext": build_ext},
    ext_modules = [Extension("asa",
        define_macros = [("ASA_LIB", "1"),
                         ("OPTIONAL_DATA_PTR", "1"),
                         ("USER_TYPE", "void *"),
                         ("USER_ASA_OUT", "1"),
                         #("ASA_PRINT_MORE", "1"),
                         #("ASA_PRINT", "0"),
                         ],
        #extra_compile_args=["-g", "-ffloat-store"],
        sources = ["src/asa.pyx", "src/asa_rand.c", "ASA/asa.c"],
        include_dirs = ["ASA", numpy.get_include(),],
        ),],
)
