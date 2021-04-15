from typing import List

import connexion
import six
from cassandra.cluster import Cluster
from werkzeug.exceptions import NotFound

from base.models import EmployeePostRequestBody
from base.models.employee import Employee  # noqa: E501
from base import util
import uuid
from typing import List


def get_employee(employee_id):  # noqa: E501
    """get_employee

    Get a list of action recommendation by targetType and targetId # noqa: E501

    :param employee_id: 
    :type employee_id: str

    :rtype: Employee
    """
    cluster = Cluster()
    session = cluster.connect('test')
    query = "SELECT * FROM employee WHERE employ_id=?"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_id,))
    rows = session.execute(bound_stsm)
    res = rows.all()
    if len(res) == 0:
        raise NotFound
    return Employee(
        employee_id=res[0].employ_id,
        name=res[0].name,
        description=res[0].description
    )


def get_employees():  # noqa: E501
    """get_employees

    get all employees # noqa: E501


    :rtype: List[Employee]
    """
    cluster = Cluster()
    session = cluster.connect('test')
    query = "SELECT * FROM employee"
    rows = session.execute(query)
    return [
        Employee(
            employee_id=row.employ_id,
            name=row.name,
            description=row.description
        ) for row in rows.all()
    ]



def delete_employee(employee_id):
    cluster = Cluster()
    session = cluster.connect('test')

    query = 'DELETE FROM employee WHERE employ_id=? ;'
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_id,))
    rows = session.execute(bound_stsm)
    return employee_id

def post_employees(employee_post_request_body=None):  # noqa: E501
    """post_employees

    create a new employee # noqa: E501

    :param employee_post_request_body:
    :type employee_post_request_body: dict | bytes

    :rtype: Employee
    """

    if connexion.request.is_json:
        employee_post_request_body = EmployeePostRequestBody.from_dict(connexion.request.get_json())  # noqa: E501

    cluster = Cluster()
    session = cluster.connect('test')
    employee_id = str(uuid.uuid4())

    query = "INSERT INTO employee (employ_id, name, description ) VALUES ( ?, ?, ?)"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_id, employee_post_request_body.name, employee_post_request_body.description,))
    rows = session.execute(bound_stsm)

    return employee_id

