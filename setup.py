# coding: utf-8

"""
    vc_webapi

    Web API for the Virtual Classroom project  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: 237294@via.dk
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "vcschedulefetch"
VERSION = "1.0.0"
DESCRIPTION = "Module that fetches calendar information for the Virtual Classroom Project from webuntis"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "docopt", "webuntis"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author='David V. Nielsen (237294)',
    author_email="237294@via.dk",
    url="",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
)



