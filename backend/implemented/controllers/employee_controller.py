from typing import List
import random
import uuid
import connexion
import six
from cassandra.cluster import Cluster
from werkzeug.exceptions import NotFound

from base.models.employee_post_request_body import EmployeePostRequestBody  # noqa: E501
from base.models.employee_put_request_body import EmployeePutRequestBody  # noqa: E501
from base.models.employee import Employee  # noqa: E501
from base import util


def delete_employee(employeeId):  # noqa: E501
    """delete_employee

    Delete a list of action recommendation by targetType and targetId # noqa: E501

    :param name:
    :type name: str

    :rtype: Employee
    """
    cluster = Cluster()
    session = cluster.connect('test2')

    query = "SELECT * FROM btiemployees WHERE id=?;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employeeId,))
    row = session.execute(bound_stsm)
    shain = row.all()

    query = "DELETE FROM btiemployees WHERE id = ?;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((id,))
    session.execute(bound_stsm)
    return shain[0].name


def get_employee(employee_id):  # noqa: E501
    cluster = Cluster()
    session = cluster.connect('test2')
    query = "SELECT * FROM btiemployees WHERE id=?;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((uuid.UUID(employee_id),))
    rows = session.execute(bound_stsm)
    res = rows.all()
    if len(res) == 0:
        raise NotFound
    return Employee(
        id=employee_id,
        name=res[0].name,
        department=res[0].department,
        omitted=res[0].omitted,
        participate=res[0].participate,
        team=res[0].team,
        mail=res[0].mail
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
    rows = session.execute("SELECT * FROM btiemployees ;")

    # random_get == True の時、omittedの値が False の社員の中からランダムで一人選んで取得する
    if random_get == True:
        name_list_shuffled = rows.all()
        random.shuffle(name_list_shuffled)
        for row in name_list_shuffled:
            if row.omitted == False:
                return [get_employee(str(row.id))]

    # participant == True の時、participateの値が True の社員を全員取得する
    elif participant == True:
        participants_list = []
        for row in rows.all():
            if row.participate == True:
                participants_list.append(get_employee(str(row.id)))
        return participants_list

    # それ以外の場合は社員を全員取得する
    else:
        return [
            Employee(
                id=row.id,
                name=row.name,
                department=row.department,
                omitted=row.omitted,
                participate=row.participate,
                team=row.team,
                mail=row.mail
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

    query = "INSERT INTO btiemployees (id,name,department,omitted,participate,team,mail) VALUES (?, ?, ?, False, False, ?, ?);"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((uuid.uuid4(), employee_post_request_body.name, employee_post_request_body.department, employee_post_request_body.team, employee_post_request_body.mail))
    session.execute(bound_stsm)

    return employee_post_request_body.name


def put_employee_by_name(employee_id, employee_put_request_body=None):  # noqa: E501
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

    query = "UPDATE btiemployees SET omitted = ? WHERE id = ? ;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_put_request_body.omitted, uuid.UUID(employee_id),))
    session.execute(bound_stsm)

    query = "UPDATE btiemployees SET participate = ? WHERE id = ? ;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_put_request_body.participate, uuid.UUID(employee_id),))
    session.execute(bound_stsm)

    query = "SELECT * FROM btiemployees WHERE id = ? ;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((uuid.UUID(employee_id),))
    row = session.execute(bound_stsm)
    shain = row.all()

    return shain[0].name


def put_employee_by_team(team_id, employee_put_request_body=None):  # noqa: E501
    """put_employee_by_team

    update omittetd and participate for the employees in the team # noqa: E501

    :param team:
    :type team: str
    :param employee_put_request_body:
    :type employee_put_request_body: dict | bytes

    :rtype: List[Employee]
    """
    if connexion.request.is_json:
        employee_put_request_body = EmployeePutRequestBody.from_dict(connexion.request.get_json())  # noqa: E501

    cluster = Cluster()
    session = cluster.connect('test2')
    rows = session.execute("SELECT * FROM btiemployees ;")
    list = []

    for row in rows.all():
        if row.team == team_id:
            put_employee_by_name(str(row.id), employee_put_request_body)
            list.append(get_employee(str(row.id)))
    return list



















# print(get_employees(random_get=True)[0].name)
# body = EmployeePutRequestBody(True,True)
# put_employee_by_name(get_employees(random_get=True)[0].name,body)
# body = EmployeePutRequestBody(False,False)
#
# put_employees('Apps',body)


