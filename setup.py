from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mfis/__init__.py
from mfis import __version__ as version

setup(
	name="mfis",
	version=version,
	description="Micro Finance Management System",
	author="Abbey",
	author_email="mugieabbeym@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
