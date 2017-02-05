import os.path

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='iso3166',
      version="0.8",
      author="Mike Spindel",
      author_email="mike@spindel.is",
      license="MIT",
      keywords="iso 3166-1 country codes",
      url="http://github.com/deactivated/python-iso3166",
      description='Self-contained ISO 3166-1 country definitions.',
      packages=find_packages(exclude=['ez_setup']),
      long_description=read('README.rst'),
      zip_safe=False,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
      ])
