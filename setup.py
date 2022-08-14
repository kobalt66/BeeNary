from setuptools import setup, find_packages

setup(
    name = "BeeNary",
    version = "1.2.1",
    description = "This package contains the interpreter for the toy language BeeNary.",
    author = "LePhobix",
    author_email = "code4beenary.gmail.com",
    url = "https://github.com/kobalt66/BeeNary",
    packages = find_packages(),
    entry_points = {
        "console_scripts" : [
            "beenary = src.BeeNary:main"
        ],
    },
)
