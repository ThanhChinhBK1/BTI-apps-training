from typing import List
import random
import connexion
import six
from cassandra.cluster import Cluster
from werkzeug.exceptions import NotFound

from base.models.employee_post_request_body import EmployeePostRequestBody  # noqa: E501
from base.models.employee_put_request_body import EmployeePutRequestBody  # noqa: E501
from base.models.employee import Employee  # noqa: E501
from base import util


def delete_employee(name):  # noqa: E501
    """delete_employee

    Delete a list of action recommendation by targetType and targetId # noqa: E501

    :param name:
    :type name: str

    :rtype: Employee
    """
    cluster = Cluster()
    session = cluster.connect('test2')

    query = "DELETE FROM btiemployee WHERE name = ?;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((name,))
    session.execute(bound_stsm)
    return name


def get_employee(name):  # noqa: E501
    """get_employee

    Get a list of action recommendation by targetType and targetId # noqa: E501

    :param name:
    :type name: str

    :rtype: Employee
    """
    cluster = Cluster()
    session = cluster.connect('test2')
    query = "SELECT * FROM btiemployee WHERE name=?"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((name,))
    rows = session.execute(bound_stsm)
    res = rows.all()
    if len(res) == 0:
        raise NotFound
    return Employee(
        name=res[0].name,
        department=res[0].department,
        omitted=res[0].omitted,
        participate=res[0].participate,
        team=res[0].team
    )


def get_employees(random_get=None, participant=None):  # noqa: E501
    """get_employees

    get employees under several conditions # noqa: E501

    :param random_get:
    :type random_get: bool
    :param participant:
    :type participant: bool

    :rtype: List[Employee]
    """
    cluster = Cluster()
    session = cluster.connect('test2')
    rows = session.execute("SELECT * FROM btiemployee ;")

    # random_get == True の時、omittedの値が False の社員の中からランダムで一人選んで取得する
    if random_get == True:
        name_list_shuffled = rows.all()
        random.shuffle(name_list_shuffled)
        for row in name_list_shuffled:
            if row.omitted == False:
                return [get_employee(row.name)]

    # participant == True の時、participateの値が True の社員を全員取得する
    elif participant == True:
        participants_list = []
        for row in rows.all():
            if row.participate == True:
                participants_list.append(get_employee(row.name))
        return participants_list

    # それ以外の場合は社員を全員取得する
    else:
        return [
            Employee(
                name=row.name,
                department=row.department,
                omitted=row.omitted,
                participate=row.participate,
                team=row.team
            ) for row in rows.all()
        ]


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
    session = cluster.connect('test2')

    query = "INSERT INTO btiemployee (name,department,omitted,participate,team) VALUES (?, ?, False, False, ?)"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_post_request_body.name, employee_post_request_body.department, employee_post_request_body.team,))

    session.execute(bound_stsm)

    return employee_post_request_body.name


def put_employee_by_name(name, employee_put_request_body=None):  # noqa: E501
    """put_employee_by_name

    update omittetd and participate for the employee # noqa: E501

    :param name:
    :type name: str
    :param employee_put_request_body:
    :type employee_put_request_body: dict | bytes

    :rtype: Employee
    """
    if connexion.request.is_json:
        employee_put_request_body = EmployeePutRequestBody.from_dict(connexion.request.get_json())  # noqa: E501

    cluster = Cluster()
    session = cluster.connect('test2')

    query = "UPDATE btiemployee SET omitted = ? WHERE name = ? ;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_put_request_body.omitted, name,))
    session.execute(bound_stsm)

    query = "UPDATE btiemployee SET participate = ? WHERE name = ? ;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_put_request_body.participate, name,))
    session.execute(bound_stsm)

    return name






















# print(get_employees(random_get=True)[0].name)
# body = EmployeePutRequestBody(True,True)
# put_employee_by_name(get_employees(random_get=True)[0].name,body)
# body = EmployeePutRequestBody(False,False)
#
# put_employees('Apps',body)


