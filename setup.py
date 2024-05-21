from os import path
from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version_file = os.path.join(path.abspath(os.path.dirname(__file__)), 'mfjet', 'version.py')
with open(version_file, 'r') as file:
    exec(file.read())

setup(
    name="mfjet",
    version=__version__,
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
