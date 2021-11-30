from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.8'
DESCRIPTION = 'Latest Cyber and Hacking News'
LONG_DESCRIPTION = 'A package that provides you Latest Cyber and Hacking News from websites using Web-Scraping.'

# Setting up
setup(
    name="cybernews",
    version=VERSION,
    author="GhoulBond",
    author_email="hitesh22rana@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['bs4', 'requests', 'lxml'],
    keywords=['python', 'web scraping', 'news', 'cyber news', 'hacker news' , 'hacking' , 'cyber' , 'free' , 'open source'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)