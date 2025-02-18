#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name="django-versionfield2",
    version="0.6.0",
    url='https://github.com/kormarun/django-versionfield',
    license='BSD',
    description="A DB Independent Custom Django Field for storing Version numbers for fast indexing",
    author='Kormarun',
    author_email='kormarun@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
    ],
    classifiers=[
        'Development Status :: 2 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
