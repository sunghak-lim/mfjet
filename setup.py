from os import path
from setuptools import find_packages, setup
from mfjet.version import VERSION

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mfjet",
    version=VERSION,
    description="Minkowski functionals in jet physics",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/sunghak-lim/mfjet",
    download_url = 'https://github.com/',
    author="Sung Hak Lim",
    packages=find_packages(exclude=["tests"]),
    license="",
    install_requires=[
        "numpy",
        "shapely",
    ],
    dependency_links=[],
)
