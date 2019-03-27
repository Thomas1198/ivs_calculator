#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Calculator',
    version='1.0',
    description='IVS 2018/2019 project',
    url='https://github.com/Thomas1198/ivs_calculator',
    package_dir={'': 'src'},
    packages=['main', 'main.modules', 'main.views'],
    py_modules=['app']
)
