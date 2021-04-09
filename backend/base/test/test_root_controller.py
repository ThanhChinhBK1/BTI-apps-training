# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from base.models.basic_response import BasicResponse  # noqa: E501
from base.test import BaseTestCase


class TestRootController(BaseTestCase):
    """RootController integration test stubs"""

    def test_ping(self):
        """Test case for ping

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/impulse-apps-training/',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
