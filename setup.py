# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-lambdata-diego", # the name that you will install via pip
    version="1.0",
    author="Diego Arriola",
    author_email="diegoarriola5@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/diegoarriola1/lambdata-diegoarriola1",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)