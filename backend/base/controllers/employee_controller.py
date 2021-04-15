import connexion
import six

from base.models.employee import Employee  # noqa: E501
from base.models.employee_post_request_body import EmployeePostRequestBody  # noqa: E501
from base import util


def delete_employee(employee_id):  # noqa: E501
    """delete_employee

    Delete a list of action recommendation by targetType and targetId # noqa: E501

    :param employee_id: 
    :type employee_id: str

    :rtype: Employee
    """
    return 'do some magic!'


def get_employee(employee_id):  # noqa: E501
    """get_employee

    Get a list of action recommendation by targetType and targetId # noqa: E501

    :param employee_id: 
    :type employee_id: str

    :rtype: Employee
    """
    return 'do some magic!'


def get_employees():  # noqa: E501
    """get_employees

    get all employees # noqa: E501


    :rtype: List[Employee]
    """
    return 'do some magic!'


def post_employees(employee_post_request_body=None):  # noqa: E501
    """post_employees

    create a new employee # noqa: E501

    :param employee_post_request_body: 
    :type employee_post_request_body: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        employee_post_request_body = EmployeePostRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
