import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "cnnClassifier"
AUTHOR_USER_NAME = "rameshucs06"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "rameshdata63@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    Long_description=long_escription,
    Long_descriiption_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"}
    packages=setuptools.find_packages(where="src")
)