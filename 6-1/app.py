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
sql = 'select * from user'
cursor.execute(sql)
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
