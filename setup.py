#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='pyworking-cz',
    version='0.0.1',
    description='Website pyworking.cz',
    url='https://github.com/pypa/sampleproject',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'doc*', 'tests']),
    install_requires=[
        'flask',
        'pyyaml',
        'markdown',
    ],
    extras_require={
        'test': ['pytest'],
    },
    include_package_data=True,
    #package_data={ 'pyworking-cz': ['pyworking_cz/templates/*', 'pyworking_cz/static/*'] },
)
