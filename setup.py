import os
from setuptools import find_packages
from setuptools import setup

base_dir = os.path.abspath(os.path.dirname(__file__))
os.chdir(base_dir)

# setup place holders for package info that comes from about.py file
name = None
description = None
version = None
uri = None
author = None
email = None
classifiers = None

with open("dataframeauditor/about.py") as about_file:
    about = about_file.read()
    exec(about)

with open('README.md') as readme_file:
    README = readme_file.read()

with open('requirements.txt') as req:
    requirements = list(filter(None, req.read().split('\n')))

EXCLUDE_FROM_PACKAGES = ['docs', 'tests*']

setup(
    name=name,
    description=description,
    long_description=README,
    long_description_content_type="text/markdown",
    version=version,
    url=uri,
    author=author,
    author_email=email,
    classifiers=classifiers,
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    install_requires=requirements,
    extras_require={},
    test_suite="tests",
    include_package_data=True
)
