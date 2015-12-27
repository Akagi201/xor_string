import os
import codecs

from setuptools import setup


def read_file(filename, encoding='utf8'):
    """Read unicode from given file."""
    with codecs.open(filename, encoding=encoding) as fd:
        return fd.read()
try:
    import pandoc
    pandoc.core.PANDOC_PATH = '/usr/local/bin/pandoc'
    doc = pandoc.Document()
    here = os.path.abspath(os.path.dirname(__file__))
    doc.markdown = read_file(os.path.join(here, 'README.md'))
    # doc.markdown = open('README.md').read()
    ld = doc.rst
except:
    ld = 'See:\nhttps://github.com/Akagi201/xor_string\n'

# here = os.path.abspath(os.path.dirname(__file__))
#
# readme = read_file(os.path.join(here, 'README.md'))

setup(
    name='xor_string',
    packages=['xor_string', ],
    version='0.2.5',
    url='https://github.com/Akagi201/xor_string',
    download_url='https://github.com/Akagi201/xor_string/tarball/0.2.5',
    description='Elegant xor encryption in Python',
    long_description=ld,
    license='MIT',
    author='Akagi201',
    author_email='akagi201@gmail.com',
    keywords=['xor', 'string', 'itertools', 'python'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Security',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
)
