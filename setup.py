import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME="Text-Summarizar-Project"
AUTHOR_USER_NAME="DheerajKumarpal1331"
SRC_REPO="textSummarizar"
AUTHOR_EMAIL="paldheeraj1331@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={"Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)