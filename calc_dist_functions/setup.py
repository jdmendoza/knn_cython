from distutils.core import setup
from Cython.Build import cythonize

setup(name="dist_cy", ext_modules=cythonize('dist_cy.pyx'),)
