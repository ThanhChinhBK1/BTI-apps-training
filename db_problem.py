import argparse
from cassandra.cluster import Cluster
import uuid


def get_employees():
    """Show all of employees."""

    cluster = Cluster()
    session = cluster.connect('test')
    rows = session.execute("SELECT * FROM employee")

    print("List of all employees:")
    for row in rows.all():
        print(row)


def create_employee(name: str, description: str):
    cluster = Cluster()
    session = cluster.connect('test')
    employee_id = str(uuid.uuid4())
    #print(str(employee_id))
    query = "INSERT INTO employee (employ_id, name, description ) VALUES ( ?, ?, ?)"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_id, name, description,))
    rows = session.execute(bound_stsm)

def get_employee(employee_id: str):
    cluster = Cluster()
    session = cluster.connect('test')
    query = "SELECT * FROM employee WHERE employ_id=?"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_id,))
    rows = session.execute(bound_stsm)
    print(rows.all())

def delete_employee(employee_id: str):
    cluster = Cluster()
    session = cluster.connect('test')
    query = "DELETE FROM employee WHERE employ_id=?"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((employee_id,))
    rows = session.execute(bound_stsm)

def main():
    """Main."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", type=str, help="Action.")
    parser.add_argument("--employee_id", help="Id of employee.")
    parser.add_argument("--name", help="Name of employee.")
    parser.add_argument("--description",
                        help="Description about the employee.")

    args = parser.parse_args()
    action = args.action
    employee_id = args.employee_id
    name = args.name
    description = args.description

    print("Action:", action)
    print("employee_id:", employee_id)
    print("name:", name)
    print("description:", description)
    print("")
    if args.action == "get_employees":
        get_employees()
    elif args.action == "create_employee":
        create_employee(name, description)
    elif args.action == "get_employee":
        get_employee(employee_id)
    elif args.action == "delete_employee":
        delete_employee(employee_id)
    else:
        print("This action is not supported!")


if __name__ == '__main__':
    main()
