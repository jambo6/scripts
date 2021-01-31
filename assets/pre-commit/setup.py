import setuptools

with open("../requirements.txt") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="sacredex",
    version="0.0.1",
    description="Custom functions for working with sacred for ML projects.",
    url="https://github.com/jambo6/sacredex",
    author="James Morrill",
    author_email="james.morrill.6@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=required,
)
