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
    packages = find_packages(exclude=('', 'CXRsegmentation')),
    package_data = {
        'testing': [
            'Testing.py'
        ]
    },
    install_requires=[
        "numpy==1.19.4",
        "torchvision==0.8.1+cu101",
        "torch==1.7.0+cu101",
        "opencv-python==4.1.2.30",
        "matplotlib==3.2.2",
        "imageio==2.4.1",
        "albumentations==0.5.2",
        "imgaug==0.4.0",
        "segmentation-models-pytorch==0.1.3",
        "sklearn==0.0",
        "pathlib==1.0.1",
        ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.9',
)
