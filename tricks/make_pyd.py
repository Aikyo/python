from distutils.core import setup
from Cython.Build import cythonize
setup(name='yuan',ext_modules = cythonize('./demo.py'))