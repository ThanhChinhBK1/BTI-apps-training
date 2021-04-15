from typing import List

import connexion
import six
from cassandra.cluster import Cluster
from werkzeug.exceptions import NotFound

from base.models.employee import Employee  # noqa: E501
from base import util


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


def delete_employee(employee_id):  # noqa: E501
    """delete_employee

    Delete a list of action recommendation by targetType and targetId # noqa: E501

    :param employee_id:
    :type employee_id: str

    :rtype: Employee
    """
    cluster = Cluster()
    session = cluster.connect('test')

    query = "DELETE FROM employee WHERE employ_id = ? ;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_id,))
    session.execute(bound_stsm)
    return employee_id
