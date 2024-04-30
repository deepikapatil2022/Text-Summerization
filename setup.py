from csv import __version__
import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

__version__ == "0.0.0"

REPO_NAME="Text-Summerization"
AUTHOR_USER_NAME="DEEPIKA"
SRC_REPO="textSummerization"
AUTHOR_EMAIL="deepikapatil2022@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__, 
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package fo NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DEEPIKA/Text-Summerization",
    project_uris={
        "Bug Tracker": f"https://github.com/DEEPIKA/Text-Summerization/issues"
    },
    
    package_dir={"": "src"}, # type: ignore
    packages=setuptools.find_packages(where="src")
    
    
)
