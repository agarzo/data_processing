# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:02:18 2020

@author: Ainara Garzo
"""

import setuptools

with open("README.adoc", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sus_questionnaire-AGARZO", # Replace with your own username
    version="0.0.1",
    author="Ainara Garzo",
    author_email="ainara.garzo@tecnalia.com",
    description="SUS (Sytem Usability Scale) questionnaire process",
    long_description=long_description,
    long_description_content_type="text/asciidoc",
    url="https://github.com/users/agarzo/projects/1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: Apache License",
        "Operating System :: Windows, Linux",
    ],
    python_requires='>=2.7',
)