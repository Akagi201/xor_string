
# import os

from setuptools import setup

# here = os.path.abspath(os.path.dirname(__file__))
# README = open(os.path.join(here, 'README.md')).read()

requires = [
    'itertools',
]

setup(
    name='xor_string',
    packages=['xor_string',],
    version='0.1.7',
    url='https://github.com/Akagi201/xor_string',
    download_url='https://github.com/Akagi201/xor_string/tarball/0.1.7',
    description='Elegant xor encryption in Python',
    # long_description=README,
    license='MIT',
    author='Akagi201',
    author_email='akagi201@gmail.com',
    keywords=['xor', 'string', 'itertools', 'python'],
    classifiers=[],
)
