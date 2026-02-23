import os
import sys
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

# 构建扩展模块
ext_modules = [
    Pybind11Extension("MathDemo",
        sources=["cpp_src/wrapper.cpp"],
        example='This is a demo package',
    ),
]

setup(
    name="MathDemo",
    version="0.0.1",
    author="Your Name",
    description="A simple example of creating a C++ extension for Python",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    zip_safe=False,
)
