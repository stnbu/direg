
from setuptools import setup

def read(file):
    with open(file, 'r') as f:
        return f.read().strip()

setup(name='direg',
    version=read('VERSION'),
    description='Drop In REGistry. Easily maintain a central configuration registry for your complex python project.',
    long_description=read('README'),
    author='Mike Burr',
    author_email='mburr@unintuitive.org',
    #install_requires=requires,
    #requires=requires,
    #classifiers=[],
    packages=['direg'],
    #package_dir={'': 'direg'},
)
