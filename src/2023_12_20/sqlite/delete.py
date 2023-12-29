# user 테이블의 데이터 삭제

import sqlite3

try:
    con = sqlite3.connect('naverDB')

    cursor = con.cursor()

    id = input('삭제할 회원ID 입력?')

    sql = 'delete from user where id = ?'

    cursor.execute(sql, (id,) )
    con.commit()
    print('삭제 성공')

    cursor.execute('select * from user')
    rows = cursor.fetchall()
    for r in rows:
        print(r[0],r[1],r[2],r[3])

except Exception as err:
    print(err)
    print('데이터베이스 연결 실패')
finally:
    con.close()