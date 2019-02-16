import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Keysort",
    version="0.1.3",
    author="Nik Kantar",
    author_email="nik@nkantar.com",
    description="A small utility for sorting lists of dictionaries by dictionary key",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/nkantar/Keysort",
    packages=setuptools.find_packages(),
)
