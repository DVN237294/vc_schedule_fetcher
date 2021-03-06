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
from openapi_client.api.videos_api import VideosApi  # noqa: E501
from openapi_client.rest import ApiException


class TestVideosApi(unittest.TestCase):
    """VideosApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.videos_api.VideosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_videos_get(self):
        """Test case for api_videos_get

        """
        pass

    def test_api_videos_id_delete(self):
        """Test case for api_videos_id_delete

        """
        pass

    def test_api_videos_id_get(self):
        """Test case for api_videos_id_get

        """
        pass

    def test_api_videos_id_put(self):
        """Test case for api_videos_id_put

        """
        pass

    def test_api_videos_post(self):
        """Test case for api_videos_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
