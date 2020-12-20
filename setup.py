import setuptools
from setuptools import setup, Extension, distutils, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CXRsegmentation", 
    version="0.0.1",
    author="CXR_team",
    author_email="dkhasanov76@gmail.com",
    description="Проект по сегментации легких.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SenpaiBabai/CXRsegmentation",
    packages = find_packages(exclude=('', 'CXRsegmentation'))
    package_data = {
        'testing': [
            'Testing.py'
        ]
    }
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License, Version 2.0",
        "Operating System :: Windows 10 / Linux (Ubuntu)",
    ],
    python_requires='>=3.6.9',
)
