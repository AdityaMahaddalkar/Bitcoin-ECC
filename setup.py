#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Aditya Mahaddalkar",
    author_email='adityam1311@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Elliptic curve cryptography implementation using secp256k1 standard (Bitcoin standard)",
    entry_points={
        'console_scripts': [
            'elliptic_curve_secp256k1=elliptic_curve_secp256k1.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='elliptic_curve_secp256k1',
    name='elliptic_curve_secp256k1',
    packages=find_packages(include=['elliptic_curve_secp256k1', 'elliptic_curve_secp256k1.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/AdityaMahaddalkar/elliptic_curve_secp256k1',
    version='0.1.0',
    zip_safe=False,
)
