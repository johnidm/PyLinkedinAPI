#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'requests',
]

test_requirements = [
    'HTTPretty',
    'sure',
]

setup(
    name='PyLinkedinAPI',
    version='0.1.4',
    description="Python library to access Liknkedin API",
    long_description=readme + '\n\n' + history,
    author="Johni Douglas Marangon",
    author_email='johni.douglas.marangon@gmail.com',
    url='https://github.com/johnidm/PyLinkedinAPI',
    packages=[
        'PyLinkedinAPI',
    ],
    package_dir={'PyLinkedinAPI':
                 'PyLinkedinAPI'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='PyLinkedinAPI',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
