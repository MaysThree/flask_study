from flask import Flask
import pymysql

# 直接import pymysql，使用pymysql连接数据库connection，不用再使用pyMySQLdb
app = Flask(__name__)
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='demo_01',
                       charset='utf8')
cursor = conn.cursor()

try:
    sql_insert1 = "insert into user(username, email) values ('hzy', '123456@163.com')"
    sql_insert2 = "insert into user(username, email) values ('maysthree', '654321@163.com')"
    cursor.execute(sql_insert1)
    cursor.execute(sql_insert2)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

sql_select = 'select * from user'
cursor.execute(sql_select)
results = cursor.fetchall()
for row in results:
    username = row[0]
    email = row[1]
    print(username, email)

cursor.close()
conn.close()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
