# -*- coding: utf-8 -*-
import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=os.getcwd().split('/')[-1],
    version="0.0.1",
    author="NAKAJIMA Takaaki",
    author_email="takaaki.nakajima.ya@d.mbsd.jp",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
