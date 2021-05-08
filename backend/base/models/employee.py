# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from base.models.base_model_ import Model
from base import util


class Employee(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, department=None, team=None, mail=None, omitted=None, participate=None):  # noqa: E501
        """Employee - a model defined in OpenAPI

        :param id: The id of this Employee.  # noqa: E501
        :type id: str
        :param name: The name of this Employee.  # noqa: E501
        :type name: str
        :param department: The department of this Employee.  # noqa: E501
        :type department: str
        :param team: The team of this Employee.  # noqa: E501
        :type team: str
        :param mail: The mail of this Employee.  # noqa: E501
        :type mail: str
        :param omitted: The omitted of this Employee.  # noqa: E501
        :type omitted: bool
        :param participate: The participate of this Employee.  # noqa: E501
        :type participate: bool
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'department': str,
            'team': str,
            'mail': str,
            'omitted': bool,
            'participate': bool
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'department': 'department',
            'team': 'team',
            'mail': 'mail',
            'omitted': 'omitted',
            'participate': 'participate'
        }

        self._id = id
        self._name = name
        self._department = department
        self._team = team
        self._mail = mail
        self._omitted = omitted
        self._participate = participate

    @classmethod
    def from_dict(cls, dikt) -> 'Employee':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Employee of this Employee.  # noqa: E501
        :rtype: Employee
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Employee.


        :return: The id of this Employee.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Employee.


        :param id: The id of this Employee.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Employee.


        :return: The name of this Employee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Employee.


        :param name: The name of this Employee.
        :type name: str
        """

        self._name = name

    @property
    def department(self):
        """Gets the department of this Employee.


        :return: The department of this Employee.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this Employee.


        :param department: The department of this Employee.
        :type department: str
        """

        self._department = department

    @property
    def team(self):
        """Gets the team of this Employee.


        :return: The team of this Employee.
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this Employee.


        :param team: The team of this Employee.
        :type team: str
        """

        self._team = team

    @property
    def mail(self):
        """Gets the mail of this Employee.


        :return: The mail of this Employee.
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail):
        """Sets the mail of this Employee.


        :param mail: The mail of this Employee.
        :type mail: str
        """

        self._mail = mail

    @property
    def omitted(self):
        """Gets the omitted of this Employee.


        :return: The omitted of this Employee.
        :rtype: bool
        """
        return self._omitted

    @omitted.setter
    def omitted(self, omitted):
        """Sets the omitted of this Employee.


        :param omitted: The omitted of this Employee.
        :type omitted: bool
        """

        self._omitted = omitted

    @property
    def participate(self):
        """Gets the participate of this Employee.


        :return: The participate of this Employee.
        :rtype: bool
        """
        return self._participate

    @participate.setter
    def participate(self, participate):
        """Sets the participate of this Employee.


        :param participate: The participate of this Employee.
        :type participate: bool
        """

        self._participate = participate
