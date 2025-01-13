import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r") as fh:
    requires = [line for line in fh.read().splitlines() if line != ""]

setuptools.setup(
    name="ao3-api",
    version="2.3.0",
    author="Wendy",
    description="An unofficial AO3 (archiveofourown.org) API",
    python_requires='>=3.8',
    install_requires=requires,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wendytg/ao3_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
