from setuptools import setup, find_packages
import flash_app

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="flash_parser",
    version=flash_app.__version__,
    author="Mandeep Dhiman",
    author_email="mandeepsinghdhiman@outlook.com",
    description="A GUI based Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MandyYdnam/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={'console_scripts':['flashapp = flash_app:main']
    }
)