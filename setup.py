#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst', encoding='utf-8') as readme_file:
    long_description = '\n' + readme_file.read()

requirements = [
    'selenium>=4.3.0',
    'Pillow>=4.0.0',
    'img2pdf>=0.2.3',
    'requests>=2.10.0'
]

setup_requirements = []

test_requirements = []

# Get the data from scribd_dlz/version.py without importing the package
exec(compile(open('scribd_dlz/version.py').read(), 'version.py', 'exec'))

setup(
    classifiers=[
        STATUS,
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Command-line program to download Scribd documents in pdf format",
    install_requires=requirements,
    license="MIT license",
    long_description=long_description,
    packages=find_packages(include=['scribd_dlz']),
    package_data={
        'scribd_dlz': ['assets/README.txt', 'version.py']
    },
    include_package_data=True,
    entry_points={
        # 'console_scripts': ['scribd-dlz = scribd_dl.scribd_dl:main']
        'console_scripts': ['scribd-dlz = scribd_dl:main']
    },
    keywords='scribd_dlz',
    name='scribd_dlz',
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Dfgsgh/scribd-dlz',
    version=VERSION,
    zip_safe=False,
)
