import pymysql.cursors

# 连接Mysql数据库
connection = pymysql.connect(host="localhost", port=3306,
                             user="root",
                             passwd="0601",
                             database="db_python",
                             charset="utf8mb4")
# cursor=pymysql.cursors.DictCursor: 以字典格式输出
try:
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = connection.cursor()
    # sql = "select * from user"
    username = "username"
    password = "password"
    cursor.execute('insert into user(id, username, password) values (6, "test", "test")')
    connection.commit()
    # res = cursor.fetchall()
    # for i in res:
    #     print(i)
    # 使用 execute()  方法执行 SQL 查询
    # cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    # data = cursor.fetchone()
    # print("Database version : %s " % data)
except Exception as e:
    print("错误信息：%s" % str(e))

finally:
    # 关闭数据库连接
    connection.close()
