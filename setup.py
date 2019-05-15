from setuptools import find_packages, setup

setup(
    name="derex.openedx",
    version="0.0.1",
    url="https://github.com/Abstract-tech/derex.openedx.git",
    author="Silvio Tomatis",
    author_email="silviot@@gmail.com",
    description="Specifications to build Open edX docker images using derex.builder",
    packages=find_packages(),
    install_requires=["derex.builder"],
)
