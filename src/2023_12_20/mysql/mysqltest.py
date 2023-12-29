# MySQL 연동 테스트

import pymysql

# 데이터베이스 접속
con = pymysql.connect(host = 'localhost',
                      user = 'root',
                      passwd = '1234',
                      port = 3306,
                      db = 'mysql',
                      charset = 'utf8')
# 커서 생성
cursor = con.cursor()

# SQL 실행
cursor.execute('select * from user')

row = cursor.fetchone()         # 1개의 데이터를 구해옴
print(type(row))                # 'tuple'
print(row)

rows = cursor.fetchall()        # 모든 데이터를 구해옴
print(type(rows))               # 'tuple'
print(rows)

for r in rows:
    print(r)

