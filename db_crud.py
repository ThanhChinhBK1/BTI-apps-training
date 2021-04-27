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

# def create_employee(namae, setsumei):
#     id = str(uuid.uuid4())
#     cluster = Cluster()
#     session = cluster.connect('test')
#
#     query = "INSERT INTO employee (employ_id, name, description) VALUES (?, ?, ?)"
#     prepared = session.prepare(query)
#     bound_stsm = prepared.bind((id,namae,setsumei,))
#
#     session.execute(bound_stsm)

def get_employee(namae):
    cluster = Cluster()
    session = cluster.connect('test')
    query = "SELECT * FROM btiemployee WHERE name = ?"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((namae,))
    row = session.execute(bound_stsm)
    # print(row)


def delete_employee(id):
    cluster = Cluster()
    session = cluster.connect('test')
    query = "DELETE FROM employee WHERE employ_id = ?"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((id,))
    session.execute(bound_stsm)


def get_employee_at_ramdom():
    cluster = Cluster()
    session = cluster.connect('test2')
    name_list = session.execute("SELECT name FROM btiemployee WHERE omitted = False ALLOW FILTERING")
    name_list_shuffled = name_list.all()
    random.shuffle(name_list_shuffled)
    print(name_list_shuffled)


def put_employee(namae):
    cluster = Cluster()
    session = cluster.connect('test2')
    query = "UPDATE btiemployee SET participate = False WHERE name = ? ;"
    prepared = session.prepare(query)
    bound_stsm = prepared.bind((namae,))
    session.execute(bound_stsm)


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
    elif args.action == "delete_employee":
        delete_employee(employee_id)
    else:
        print("This action is not supported!")


if __name__ == '__main__':
    main()

