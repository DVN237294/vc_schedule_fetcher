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
from openapi_client.api.comments_api import CommentsApi  # noqa: E501
from openapi_client.rest import ApiException


class TestCommentsApi(unittest.TestCase):
    """CommentsApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.comments_api.CommentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_comments_id_delete(self):
        """Test case for api_comments_id_delete

        """
        pass

    def test_api_comments_post(self):
        """Test case for api_comments_post

        """
        pass

    def test_api_comments_video_id_get(self):
        """Test case for api_comments_video_id_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
