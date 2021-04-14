# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from base.models.employee import Employee  # noqa: E501
from base.test import BaseTestCase


class TestEmployeeController(BaseTestCase):
    """EmployeeController integration test stubs"""

    def test_get_employee(self):
        """Test case for get_employee

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/impulse-apps-training/employees/{employee_id}'.format(employee_id='employee_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_employees(self):
        """Test case for get_employees

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/impulse-apps-training/employees',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
