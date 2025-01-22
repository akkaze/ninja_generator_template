#!/usr/bin/env python

"""Ninja build configurator for greeter library"""

import sys
import os

sys.path.insert(0, os.path.join("..", "ninja_generator"))

import generator

generator = generator.Generator(project="greeter")

greeter_lib = generator.lib(
    module="src",
    libname="greeter",
    sources=["greeter.cpp"],
    includepaths=["include"],
    variables={"runtime": "c++", "defines": ["ENABLE_DYNAMIC_LINK=1"]},
)

greeter_so = generator.sharedlib(
    module="src",
    libname="greeter",
    sources=["greeter.cpp"],
    includepaths=["include"],
    variables={"runtime": "c++", "defines": ["ENABLE_DYNAMIC_LINK=1"]},
)

generator.bin(
    module="src",
    sources=["main.cpp"],
    binname="main",
    implicit_deps=[greeter_so],
    libs=["greeter"],
    includepaths=["include"],
    variables={"runtime": "c++", "defines": ["ENABLE_ASSERTS=1",]},
)
