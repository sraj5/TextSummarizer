import setuptools

with open("README.md","r",encoding="utf-8")as f:  #opening the Readme file in read mode and using utf-8 encoding. We will use it as long description
    long_description=f.read()   #take the whole readme file's content as long_description
    
__version__="0.0.0"

#github details
REPO_NAME = "textsummarizer"   
AUTHOR_USER_NAME = "sraj5"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "rajsaurabh2138@gmail.com"

#using setuptools library to make the setup
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)  