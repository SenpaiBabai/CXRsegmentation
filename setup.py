import setuptools
from setuptools import setup, Extension, distutils, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SiriusN16CXRseg", 
    version="0.0.1",
    author="Sirius_nauka16",
    author_email="dkhasanov76@gmail.com",
    description="Проект по сегментации легких.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SenpaiBabai/CXRsegmentation",
    packages = find_packages(),
    package_data = {
        'CXRsegmentation': [
            'trained_models/Model_lungs_heart',
        ]
    },
    install_requires=[
        "numpy==1.19.4",
        "torchvision==0.8.1",
        "torch==1.7.0",
        "opencv-python==4.1.2.30",
        "matplotlib==3.2.2",
        "imageio==2.4.1",
        "albumentations==0.5.2",
        "imgaug==0.4.0",
        "segmentation-models-pytorch==0.1.3",
        "sklearn==0.0",
        "pathlib==1.0.1",
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.9',
)
