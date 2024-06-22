from setuptools import setup, find_packages
import codecs
import os

HERE = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.0'
DESCRIPTION = 'DockF-Sec-Check helps to make your Dockerfile commands more secure.'
# Setting up
setup(
    name="DocFSecCheck",
    version=VERSION,
    author="OsmanKandemir",
    author_email="osmankandemir00[@]gmail[.]com",
    license='GPL-3.0',
    url='https://github.com/OsmanKandemir/docf-sec-check',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    packages=find_packages(),
    install_requires=[
        "urllib3==1.26.14"
    ],
    keywords=['python', 'dockerfile','docker','security-tools'],
    classifiers=[
    
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Natural Language :: English",
        "Environment :: Console",
        "Topic :: Security",
        "Typing :: Typed",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Telecommunications Industry",
        "Intended Audience :: System Administrators"
    ],
    python_requires='>=3.9',
)