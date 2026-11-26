from setuptools import setup
from Cython.Build import cythonize

setup(name='sum_squares', ext_modules=cythonize('sum_squares.pyx', language_level=3))
