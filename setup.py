#!/usr/bin/env python
"""A setuptools based setup module for PyJson2C"""
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='PyJson2C',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Python's C Linter",
    long_description=readme + '\n\n' + history,
    author="jmramosr",
    author_email='https://github.com/jmramosr',
    url='https://github.com/jmramosr/PyJson2C',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts': [
            'PyJson2C=PyJson2C.PyJson2C:PyJson2CMain',
            ],
        },
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPLv3',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)

# Add to the setup Classifiers if you want support with other Python Versions
#        "Programming Language :: Python :: 2",
#        'Programming Language :: Python :: 2.7',
#        'Programming Language :: Python :: 3',
#        'Programming Language :: Python :: 3.3',
#        'Programming Language :: Python :: 3.4',
#        'Programming Language :: Python :: 3.5',
