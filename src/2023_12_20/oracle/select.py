# dept 테이블의 데이터 검색

import cx_Oracle

try:
    con = cx_Oracle.connect('scott/tiger@localhost:1521/xe')
    cursor = con.cursor()

    no = input('검색할 부서번호를 입력하세요?')

    sql = "select * from dept where deptno = :no"

    cursor.execute(sql, no = no)
    rows = cursor.fetchall()            # 모든 데이터를 구해옴
    for r in rows:
        print(r[0], r[1], r[2])

except Exception as err:
    print(err)
finally:
    con.close()