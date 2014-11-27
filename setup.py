
from setuptools import setup

def read(file):
    with open(file, 'r') as f:
        return f.read().strip()

setup(name='direg',
    version=read('VERSION'),
    description='A drop-in registry. Easily maintain a central configuration registry for your complex python project.',
    long_description=read('README.rst'),
    author='Mike Burr',
    author_email='mburr@unintuitive.org',
    url='https://github.com/stnbu/direg',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    packages=['direg'],
    keywords=['configuration', 'registry', 'refactor'],
)
