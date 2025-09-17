from setuptools import setup, find_packages

print(find_packages())

setup(
    name="cool_package",
    version="0.0.1",
    description="this package is a template for fullstack app",
    author="Kokchun",
    author_email="author@mail.se",
    packages=find_packages(),
)