import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cs46_ekurztrees",
    version="1.0.0",
    description="Implementation of Binary Trees, BST, AVL, and Heap Tree structures",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ekurz20/trees",
    author="ekurz20",
    author_email="ekurz20@cmc.edu",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["Trees"],
    install_requires=["pytest", "hypothesis"],
)
