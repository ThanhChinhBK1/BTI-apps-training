from cassandra.cluster import Cluster
import random

def get_employee(name):  # noqa: E501
    """get_employee

    Get a list of action recommendation by targetType and targetId # noqa: E501

    :param employee_id:
    :type employee_id: str

    :rtype: Employee
    """
    cluster = Cluster()
    session = cluster.connect('test2')
    query = "SELECT * FROM employee WHERE name=?"
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

if __name__ == "__main__":

    # 　初期化
    cluster = Cluster()
    # 　データベースに接続
    session = cluster.connect('test2')

    rows = session.execute("SELECT * FROM btiemployee ;")
    name_list_shuffled = rows.all()
    random.shuffle(name_list_shuffled)
    for row in name_list_shuffled:
        if row.omitted == False:
            print([get_employee(row.name)])
            break;

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


    # Query with parameter
    # query = "INSERT INTO btiemployee ( name, department, omitted ) VALUES (?, ?, ?);"
    # prepared = session.prepare(query)
    # bound_stsm = prepared.bind(('鈴木 誠二郎', '特別', False))
    # rows = session.execute(bound_stsm)
    # bound_stsm = prepared.bind(('前田 昌太朗', '特別', False))
    # rows = session.execute(bound_stsm)
    # bound_stsm = prepared.bind(('本間 由美子', '特別', False))
    # rows = session.execute(bound_stsm)
    # bound_stsm = prepared.bind(('柏木 琴真', '製品開発部', False))
    # rows = session.execute(bound_stsm)
    # bound_stsm = prepared.bind(('矢羽々 豊', 'プロダクトマネジメント部', False))
    # rows = session.execute(bound_stsm)
    # bound_stsm = prepared.bind(('Le Hau', '未来ラボ', False))
    # rows = session.execute(bound_stsm)

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




