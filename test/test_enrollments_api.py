# coding: utf-8

"""
    vc_webapi

    Web API for the Virtual Classroom project  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: 237294@via.dk
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.enrollments_api import EnrollmentsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestEnrollmentsApi(unittest.TestCase):
    """EnrollmentsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.enrollments_api.EnrollmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_enrollments_my_enrollments_get(self):
        """Test case for api_enrollments_my_enrollments_get

        """
        pass

    def test_api_enrollments_post(self):
        """Test case for api_enrollments_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
