from cassandra.cluster import Cluster
import random
import uuid

if __name__ == "__main__":

    # 　初期化
    cluster = Cluster()
    # 　データベースに接続
    session = cluster.connect('test2')

    # query = "SELECT * FROM btiemployees WHERE id=?;"
    # prepared = session.prepare(query)
    # bound_stsm = prepared.bind((uuid.UUID('1f66b07b-1c7d-4706-a03f-51b9bfece190'),))
    # row = session.execute(bound_stsm)
    # shain = row.all()
    # print(shain[0].name)

    rows = session.execute("SELECT * FROM btiemployees ;")
    list = []

    for row in rows.all():
        query = "UPDATE btiemployees SET omitted = False WHERE id=? ;"
        prepared = session.prepare(query)
        bound_stsm = prepared.bind((row.id,))
        session.execute(bound_stsm)
        query = "UPDATE btiemployees SET participate = False WHERE id=? ;"
        prepared = session.prepare(query)
        bound_stsm = prepared.bind((row.id,))
        session.execute(bound_stsm)





    # Query with parameter
    # query = "INSERT INTO btiemployees (id, name, department, mail, omitted, participate, team) VALUES (?,?,?,?,?, ?, ?);"
    # prepared = session.prepare(query)
    # bound_stsm = prepared.bind((uuid.uuid4(), '西川 浩平', '製品開発部', None, False, False, 'PS'))
    # rows = session.execute(bound_stsm)
    # bound_stsm = prepared.bind((uuid.uuid4(), '前田 昌太朗', '社外', None, False, False, '社外'))
    # rows = session.execute(bound_stsm)
    # bound_stsm = prepared.bind((uuid.uuid4(), '本間 由美子', '社外', None, False, False, '社外'))
    # rows = session.execute(bound_stsm)
    # bound_stsm = prepared.bind((uuid.uuid4(), '柏木 琴真', '社外', None, False, False, '社外'))
    # rows = session.execute(bound_stsm)
    # bound_stsm = prepared.bind((uuid.uuid4(), '矢羽々 豊', '社外', None, False, False, '社外'))
    # rows = session.execute(bound_stsm)
    # bound_stsm = prepared.bind((uuid.uuid4(), 'Le Hau', '社外', None, False, False, '社外'))
    # rows = session.execute(bound_stsm)


    # name_list = []
    #
    # rows = session.execute("SELECT * FROM btiemployee ;")
    # name_list_shuffled = rows.all()
    # random.shuffle(name_list_shuffled)
    # for row in name_list_shuffled:
    #         name_list.append(row.name)
    # print(name_list)
    # query = "UPDATE btiemployee2 SET omitted = True WHERE name=';"
    # prepared = session.prepare(query)
    # bound_stem = prepared.bind(('中澤 貴明',))
    # session.execute(bound_stem)
    #
    # query = "UPDATE btiemployee SET participate = False WHERE name = ? ;"
    # prepared = session.prepare(query)
    # bound_stem = prepared.bind(('竹内 沙也加',))
    # session.execute(bound_stem)
    #
    # query = "UPDATE btiemployee SET participate = False WHERE name = ? ;"
    # prepared = session.prepare(query)
    # bound_stem = prepared.bind(('原 拓郎',))
    # session.execute(bound_stem)
    #
    # query = "UPDATE btiemployee SET participate = False WHERE name = ? ;"
    # prepared = session.prepare(query)
    # bound_stem = prepared.bind(('石本 慎太郎',))
    # session.execute(bound_stem)
    #
    # query = "UPDATE btiemployee SET participate = False WHERE name = ? ;"
    # prepared = session.prepare(query)
    # bound_stem = prepared.bind(('吉田 香織',))
    # session.execute(bound_stem)
    #
    # query = "UPDATE btiemployee SET participate = False WHERE name = ? ;"
    # prepared = session.prepare(query)
    # bound_stem = prepared.bind(('Le Hau',))
    # session.execute(bound_stem)
    #
    # query = "UPDATE btiemployee SET participate = False WHERE name = ? ;"
    # prepared = session.prepare(query)
    # bound_stem = prepared.bind(('奥山 昌紀',))
    # session.execute(bound_stem)
    #
    # query = "UPDATE btiemployee SET participate = False WHERE name = ? ;"
    # prepared = session.prepare(query)
    # bound_stem = prepared.bind(('藤原 和成',))
    # session.execute(bound_stem)
    #
    # query = "UPDATE btiemployee SET participate = False WHERE name = ? ;"
    # prepared = session.prepare(query)
    # bound_stem = prepared.bind(('河田 哲',))
    # session.execute(bound_stem)
    #
    # query = "UPDATE btiemployee SET participate = False WHERE name = ? ;"
    # prepared = session.prepare(query)
    # bound_stem = prepared.bind(('西川 浩平',))
    # session.execute(bound_stem)


    # rows = session.execute("SELECT * FROM btiemployee WHERE omitted = False ALLOW FILTERING")
    # row = rows.all()[0]
    # print(row.name, row.department, row.team, row.omitted, row.participate)
    # name_list = session.execute("SELECT name FROM btiemployee WHERE omitted = False ALLOW FILTERING")
    # name_list_shuffled = name_list.all()
    # print(type(name_list_shuffled[0]))
    # random.shuffle(name_list_shuffled)
    # print(name_list_shuffled[0].name, name_list_shuffled[0].count)
    # name_list_shuffled[0].participate = true
    # print(name_list_shuffled[0].name, name_list_shuffled[0].participate)

    # rows = session.execute("SELECT * FROM btiemployee WHERE omitted=False ALLOW FILTERING")
    # name_list_shuffled = rows.all()
    # random.shuffle(name_list_shuffled)
    # for row in name_list_shuffled:
    #     if row.omitted == False:
    #         query = "UPDATE btiemployee SET participate=True WHERE name=?;"
    #         prepared = session.prepare(query)
    #         bound_stsm = prepared.bind((row.name,))
    #         session.execute(bound_stsm)
    #
    #         query = "UPDATE btiemployee SET omitted=True WHERE name=?;"
    #         prepared = session.prepare(query)
    #         bound_stsm = prepared.bind((row.name,))
    #         session.execute(bound_stsm)
    #
    #         query = "SELECT * FROM btiemployee WHERE name = ?;"
    #         prepared = session.prepare(query)
    #         bound_stsm = prepared.bind((row.name,))
    #         row = session.execute(bound_stsm)
    #
    #         break;




