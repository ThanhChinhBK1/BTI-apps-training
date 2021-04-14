import argparse
import uuid

from cassandra.cluster import Cluster


def get_employees():
    """Show all of employees."""

    cluster = Cluster()
    session = cluster.connect('test')
    rows = session.execute("SELECT * FROM employee")

    print("List of all employees:")
    for row in rows.all():
        print(row)

def create_employee(namae, setsumei):
    id = uuid.uuid4()
    cluster = Cluster()
    session = cluster.connect('test')

    session.execute("INSERT INTO employee (employ_id, name, description) VALUES (id, 'namae', 'setsumei')")

def get_employee(id):
    cluster = Cluster()
    session = cluster.connect('test')
    row = session.execute("SELECT * FROM employee WHERE employ_id = 'id'")
    print(row)

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
    elif args.action == "...":
        # TODO implement method for create_employee, get_employee, delete_employee
        print("Do something to ")
    elif args.action == "create_employee":
        create_employee(name,description)
    elif args.action == "get_employee":
        get_employee(employee_id)
    else:
        print("This action is not supported!")


if __name__ == '__main__':
    main()


