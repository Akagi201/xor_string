import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()

requires = [
    'itertools',
]

setup(name='xor-string',
      version='0.1.0',
      url='https://github.com/Akagi201/xor-string',
      description='Elegant xor encryption in Python',
      long_description=README,
      license='MIT License',
      packages=[
          'xor_string',
      ],
      author='Akagi201',
      author_email='akagi201@gmail.com',
      keywords='xor string',
      ),
)
