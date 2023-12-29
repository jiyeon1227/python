# user 테이블 데이터 수정

import sqlite3

try:
    con = sqlite3.connect('naverDB')

    cursor = con.cursor()

    id = input('수정할 회원ID 입력?')
    email = input('수정할 EMail 주소 입력?')

    sql = "update user set email=? where id=?"
    cursor.execute(sql, (email, id))

    con.commit()

    cursor.execute('select * from user')
    rows = cursor.fetchall()
    for r in rows:
        print(r[0],r[1],r[2],r[3])

except Exception as err:
    print(err)
    print('데이터베이스 열결 실패')
finally:
    con.close()