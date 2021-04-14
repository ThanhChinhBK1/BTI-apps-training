from cassandra.cluster import Cluster
if __name__ == "__main__":
    print("db_test")

    # 　初期化
    cluster = Cluster()
    # 　データベースに接続
    session = cluster.connect('test')
    # 　Query
    rows = session.execute("SELECT * FROM employee")
    print(rows.all())
    # Query with parameter
    query = "INSERT INTO employee (employ_id, name, description ) VALUES (?, ?, ?) ;"

    prepared = session.prepare(query)
    bound_stsm = prepared.bind(('BR3', 'Urashimataro', 'A boy',))
    rows = session.execute(bound_stsm)
    print(rows.all())
