# user 테이블의 데이터 검색

import sqlite3

try:
    # 데이터베이스 접속
    con = sqlite3.connect('naverDB')

    cursor = con.cursor()

    cursor.execute('select * from user')

    print('사용자ID\t 사용자 이름\t 이메일\t 생년월일')
    print('---------------------------------------')

    # row = cursor.fetchone()                 # 1개의 데이터 검색
    # print(type(row))                        # <class 'tuple'>
    # print(row)                              # ('test', '안화수', 'test@b.com', '1995.12.02')

    rows = cursor.fetchall()                  # 모든 데이터 검색
    print(type(rows))                         # <class 'list'>
    print(rows)

    for r in rows:
        print(r[0], r[1], r[2], r[3])

except Exception as err:
    print(err)
    print('데이터베이스 연결 실패')
finally:
    con.close()