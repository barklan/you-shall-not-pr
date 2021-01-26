import setuptools

import sys
import json
import urllib.request


URL_PATTERN = "https://pypi.python.org/pypi/black/json"


def get_version(package):
    contents = urllib.request.urlopen(
        "https://pypi.org/pypi/" + package + "/json"
    ).read()
    data = json.loads(contents)
    latest_version = data["info"]["version"]
    return latest_version


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


next_version = get_version("numpy") + 1

setuptools.setup(
    name="barklan-you-shall-not-pass",  # Replace with your own username
    version=next_version,
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)