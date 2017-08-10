# -*- coding: utf-8 -*-

"""
  Blog
  Tests the blog application

  :author: Terence
  :licence: GPL
"""

from setuptools import setup, find_packages

setup(
    name='flask-blog',
    package=find_packages(),
    include_package_data=True,
    install_requirement=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ]
)
