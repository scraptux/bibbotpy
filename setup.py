# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='bibbot',
    version='0.0.1',
    description='BibBot bucht dir ein Sitzplatz in der Bib, sobald es verfügbar ist',
    long_description=readme,
    author='scraptux',
    url='https://github.com/scraptux/bibbotpy',
    license=license,
    packages=find_packages()
)