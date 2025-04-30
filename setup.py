from setuptools import setup, find_packages
import pathlib

long_description = pathlib.Path("README.md").read_text(encoding="utf-8")

setup(
    name="nprxchange",
    version="0.1.1",
    description="Nepal Rastra Bank Currency Converter",
    long_description= long_description,
    long_description_content_type="text/markdown",
    author="Munal Poudel",
    author_email="munalpoudel3@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "rich>=14.0.0",
        "InquirerPy>=0.3.4",
    ],
    entry_points={
        "console_scripts": [
            "nprxchange=nprxchange.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)