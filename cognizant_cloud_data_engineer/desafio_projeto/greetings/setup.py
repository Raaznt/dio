from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="greetings",
    version="0.0.1",
    author="Raimundo Azevedo",
    author_email="raaznt@gmail.com",
    description="Pacote criado como desafio de código no curso da DIO.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="github.com/raaznt/greetings.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)