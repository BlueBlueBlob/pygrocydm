import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygrocydm",
    version="0.7.0",
    author="Blueblueblob",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlueBlueBlob/pygrocydm",
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "iso8601",
        "pytz",
        "tzlocal"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
