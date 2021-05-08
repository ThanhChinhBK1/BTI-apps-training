import connexion
import six

from base.models.employee import Employee  # noqa: E501
from base.models.employee_post_request_body import EmployeePostRequestBody  # noqa: E501
from base.models.employee_put_request_body import EmployeePutRequestBody  # noqa: E501
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


def get_employees(random_get=None, participant=None):  # noqa: E501
    """get_employees

    get employees under several conditions # noqa: E501

    :param random_get: 
    :type random_get: bool
    :param participant: 
    :type participant: bool

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


def put_employee_by_name(employee_id, employee_put_request_body=None):  # noqa: E501
    """put_employee_by_name

    update omittetd and participate for the employee # noqa: E501

    :param employee_id: 
    :type employee_id: str
    :param employee_put_request_body: 
    :type employee_put_request_body: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        employee_put_request_body = EmployeePutRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_employee_by_team(team_id, employee_put_request_body=None):  # noqa: E501
    """put_employee_by_team

    update omittetd and participate for the employees in the team # noqa: E501

    :param team_id: 
    :type team_id: str
    :param employee_put_request_body: 
    :type employee_put_request_body: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        employee_put_request_body = EmployeePutRequestBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
