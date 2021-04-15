# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from base.models.base_model_ import Model
from base import util


class EmployeePutRequestBody(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None):  # noqa: E501
        """EmployeePutRequestBody - a model defined in OpenAPI

        :param description: The description of this EmployeePutRequestBody.  # noqa: E501
        :type description: str
        """
        self.openapi_types = {
            'description': str
        }

        self.attribute_map = {
            'description': 'description'
        }

        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'EmployeePutRequestBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EmployeePutRequestBody of this EmployeePutRequestBody.  # noqa: E501
        :rtype: EmployeePutRequestBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this EmployeePutRequestBody.


        :return: The description of this EmployeePutRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EmployeePutRequestBody.


        :param description: The description of this EmployeePutRequestBody.
        :type description: str
        """

        self._description = description
