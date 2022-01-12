import pandas as pd
from sqlalchemy import create_engine

# 初始化数据库连接
# 按实际情况依次填写MySQL的用户名、密码、IP地址、端口、数据库名
# engine = create_engine('mysql+pymysql://root:12345678@localhost:3306/testdb')
if __name__ == "__main__":
    # 如果觉得上方代码不够优雅也可以按下面的格式填写:用户名、密码、IP地址、端口、数据库名
    engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('root', '0601', 'localhost', '3306', 'db_python'))
# MySQL导入DataFrame
# 填写自己所需的SQL语句，可以是复杂的查询语句
# sql_query = "select * from user"
# # 使用pandas的read_sql_query函数执行SQL语句，并存入DataFrame
# df_res = pd.read_sql_query(sql_query, engine)
# print(df_res)

nameList = ["abc", "def", "ghj"]
pswdList = ["qwe", "qwe", "qwe"]
if __name__ == "__main__":
    df_write = pd.DataFrame({
        "username": nameList,
        "password": pswdList
    })
    df_write.to_sql("test_user_3", engine)
