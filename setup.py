#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='ptwitter',
    version='0.0.1',
    description="Tiny python library for Twitter's REST API.",
    author='Mitchel Kelonye',
    author_email='kelonyemitchel@gmail.com',
    url='https://github.com/kelonye/python-twitter',
    packages=['ptwitter',],
    package_dir = {'ptwitter': 'lib'},
    license='MIT License',
    zip_safe=True)
