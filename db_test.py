from cassandra.cluster import Cluster

if __name__ == "__main__":
    print("db_test")



    # 　初期化
    cluster = Cluster()
    # 　データベースに接続
    session = cluster.connect('test')
    # 　Query

    query = "INSERT INTO employee (employ_id, name, description )VALUES ( ?, ?, ?);"
    rows = session.execute("SELECT * FROM employee")
    print(rows.all())

    # Query with parameter
    prepared = session.prepare(query)
    bound_stsm = prepared.bind(('BR1','owari','sample'))
    rows = session.execute(bound_stsm)
    rows = session.execute("SELECT * FROM employee")
    print(rows.all())
