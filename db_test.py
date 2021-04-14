from cassandra.cluster import Cluster

# 　初期化
cluster = Cluster()
# 　データベースに接続
session = cluster.connect('test')
# 　Query
#rows = session.execute("INSERT INTO employee (employ_id, name, description ) VALUES ( 'BR4', 'Queen', 'Beautiful')")

rows = session.execute("SELECT * FROM employee")
print(rows.all())

# Query with parameter
# query = "SELECT * FROM employee WHERE employ_id=?"
query = "INSERT INTO employee (employ_id, name, description ) VALUES ( ?, ?, ?)"
prepared = session.prepare(query)
bound_stsm = prepared.bind(('BR6','ace','nice',))
rows = session.execute(bound_stsm)

rows = session.execute("SELECT * FROM employee")
print(rows.all())
