from setuptools import setup, find_packages
import os
import codecs

VERSION = '0.1'
DESCRIPTION = 'This is a simple library with many useful and simple tools.'

# Setting up
setup(
    name="XToolsLib",
    version=VERSION,
    author="Mr Abood",
    author_email="XTools@outlook.sa",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests", "requests[socks]"],
    keywords=['XToolsLib'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)