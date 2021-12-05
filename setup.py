"""stac-check setup.py
"""
from setuptools import setup

__version__ = "0.1.3"

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="stac_check",
    version=__version__,
    description="Linting and validation tool for STAC assets",
    url="https://github.com/jonhealy1/stac-check",
    packages=["stac_check"],
    install_requires=[
        "click>=7.1.2",
        "pystac[validation]==1.1.0",
        "requests>=2.19.1",
        "jsonschema>=3.1.2b0",
        "pytest>=6.0.0"
    ],
    entry_points={
        'console_scripts': ['stac_check=stac_check.cli:main']
    },
    author="Jonathan Healy",
    author_email="jonatham.d.healy@gmail.com",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    tests_require=["pytest"]
)