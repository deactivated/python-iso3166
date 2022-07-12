import os.path

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="iso3166",
    version="2.1.0",
    author="Mike Spindel",
    author_email="mike@spindel.is",
    license="MIT",
    keywords="iso 3166-1 country codes",
    url="http://github.com/deactivated/python-iso3166",
    description="Self-contained ISO 3166-1 country definitions.",
    packages=find_packages(),
    package_data={
        "iso3166": ["py.typed"],
    },
    long_description=read("README.rst"),
    zip_safe=False,
    python_requires=">= 3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
