# 데이터베이스와 테이블 생성

import sqlite3

# 데이터베이스 생성 함수
def create_table():
   con = sqlite3.connect('naverDB')      # 데이터베이스 생성 및 연결

   cursor = con.cursor()                 # 커서 생성

   # user 테이블 생성
   cursor.execute('''create table user(
                       id char(20),
                       username char(20),
                       email char(20),
                       birth char(20) )
                  ''')

   con.commit()
   con.close()

if __name__=='__main__':
    create_table()              # 함수 호출


