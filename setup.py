import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = ''

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: Apache Software License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.6',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(
    name         = 'FaBoGPIO_PCAL6408',
    version      = '1.0.2',
    author       = 'FaBo',
    author_email = 'info@fabo.io',
    description  = "This is a library for the FaBo GPIO I2C Brick.",
    long_description=long_description,
    url          = 'https://github.com/FaBoPlatform/FaBoGPIO-PCAL6408-Python/',
    license      = 'Apache License 2.0',
    classifiers  = classifiers,
    packages     = find_packages()
)
