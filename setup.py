#!/usr/bin/env python3

from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='camaptools',
    version='0.1.0',
    author='Albert Feghaly',
    author_email='albert.feghaly@gmail.com',
    url='https://epitopes.world',
    description='Codon Arrangement MAP Predictor (CAMAP) Tools',
    long_description=long_description,
    license='MIT',
    package_dir={'camaptools': 'camaptools'},
    packages=['camaptools'],
    install_requires=[
        'numpy==1.18.1',
        'scikit-learn==1.5.0',
        'parse==1.6.6'
    ],
    python_requires='>=3.5',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
)
