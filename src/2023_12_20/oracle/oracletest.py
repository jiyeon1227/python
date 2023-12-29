# python과  oracle 연동 테스트

import cx_Oracle

try:
    # 데이터베이스 접속
    # con = cx_Oracle.connect('아이디/암호@아이피:1521/인스턴스명')
    con = cx_Oracle.connect('scott/tiger@localhost:1521/xe')
    # con = cx_Oracle.connect('totoro/totoro123@localhost:1521/xe')
    # con = cx_Oracle.connect('system/ora123@localhost:1521/xe')
    
    cursor = con.cursor()
    
    cursor.execute('select * from dept')
    # cursor.execute('select * from board0')

    row = cursor.fetchone()             # 데이터 1개를 구해옴
    print(type(row))                    # <class 'tuple'>
    print(row)                          # (10, 'ACCOUNTING', 'NEW YORK')

    rows = cursor.fetchall()            # 모든 데이터를 구해옴
    print(type(rows))                   # <class 'list'>
    print(rows)

except Exception as err:
    print(err)
finally:
    con.close()