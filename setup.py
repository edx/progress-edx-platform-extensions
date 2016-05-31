#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='progress-edx-platform-extensions',
    version='1.0.1',
    description='Progress management extension for edX platform',
    long_description=open('README.rst').read(),
    author='edX',
    url='https://github.com/edx-solutions/progress-edx-platform-extensions',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=1.4,<1.5",
    ],
)
