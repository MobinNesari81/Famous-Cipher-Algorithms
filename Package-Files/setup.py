from setuptools import setup, find_packages

VERSION = '0.1.4'
DESCRIPTION = 'Famous Cipher Algorithms'
LONG_DESCRIPTION = 'FamousCipherAlgorithms is a Python package for implementing a variety of cryptographic ciphers and encryption methods, designed to provide secure and reliable data protection.'

setup(
    name='FamousCipherAlgorithms',
    version=VERSION,
    author='Mobin Nesari',
    author_email='mobinnesari81@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    url='https://famous-cipher-algorithm.readthedocs.io/en/latest/index.html',
    keywords=['Python', 'Cipher', 'Cryptography', 'Algorithms'],
    classifiers=["Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            'Operating System :: POSIX'],
)
