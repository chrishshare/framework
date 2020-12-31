# coding: utf-8

from setuptools import setup
from setuptools import find_packages
import io


def read_file(filename):
    with io.open(filename, 'r', encoding='UTF-8') as fp:
        return fp.read().strip()


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup(
    name="framework",
    include_package_data=True,
    version="0.0.1",
    author="chrishshare",
    author_email="chrishshare@163.com",
    description="framework",
    license="MIT",
    keywords="framework",
    url="https://github.com/chrishshare/framework",
    packages=find_packages("framework"),  # include all packages under src
    package_dir={'': 'framework'},
    # install_requires=read_requirements('framework/requirements.txt'),
    package_data={
        "framework": ["config/logger.json", "config/projectConfig.yaml", "libs/mysql-connector-java-8.0.16.jar",
                      "libs/ojdbc6.jar", "libs/sqlite-jdbc-3.28.0.jar"]}
)
# python setup.py bdist_wheel
