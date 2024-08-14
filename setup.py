import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "ML_Project_MLFlow_AWS"
AUTHOR_UNAME = "Empyrean1001"
SRC_REPO = "ML-project"
AUTHOR_MAIL = "devkrishnajhawar@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_UNAME,
    author_email = AUTHOR_MAIL,
    description = "A trial python package for ML App",
    Long_description = long_description,
    Long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_UNAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_UNAME}/{REPO_NAME}/issues",
    },
    package_dir = {"" : "src"},
    packages = setuptools.find_packages(where="src")

)