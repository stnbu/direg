# -*- coding: utf-8 -*-

from setuptools import setup

import direg

# README.rst dynamically generated:
with open('README.rst', 'w') as f:
    f.write(direg.__doc__)

NAME = 'direg'

def read(file):
    with open(file, 'r') as f:
        return f.read().strip()

setup(
    name=NAME,
    version=read('VERSION'),
    description=('A drop-in registry. Easily maintain a central configuration registry for your complex '
                 'python project.'),
    long_description='\n' + read('README.rst'),
    author='Mike Burr',
    author_email='mburr@unintuitive.org',
    url='https://github.com/stnbu/{0}'.format(NAME),
    download_url='https://github.com/stnbu/{0}/archive/master.zip'.format(NAME),
    provides=[NAME],
    license='MIT',
    bugtrack_url='https://github.com/stnbu/{0}/issues'.format(NAME),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    packages=[NAME],
    keywords=['configuration', 'registry', 'refactor'],
    test_suite='nose.collector',
    test_requires=['nose'],
)
