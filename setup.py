#!/usr/bin/env python

import os
import sys

import srccat

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = ['srccat', 'tests']

requires = ['colout']

setup(
    name='srccat',
    version='0.1',
    description='Syntax highlights source code to terminal using colout',
    long_description=open('README.md').read(),
    author='cfeduke',
    author_email='charles.feduke@gmail.com',
    url='http://cfeduke.github.com/srccat/',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'srccat': 'srccat'},
    scripts=['bin/srccat'],
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
)
