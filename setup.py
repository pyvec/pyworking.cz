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
        'flask<2',  # ImportError: cannot import name 'Markup' from 'jinja2'
        'ics',
        'pyyaml',
        'markdown<3.4',  # https://github.com/r0wb0t/markdown-urlize/pull/17
        'markdown-urlize',
        'markupsafe<2.1.0',  # ImportError: cannot import name 'soft_unicode' from 'markupsafe'
        'pytz',
        'requests',
        'Frozen-Flask',
    ],
    extras_require={
        'test': ['pytest'],
    },
    include_package_data=True,
)
