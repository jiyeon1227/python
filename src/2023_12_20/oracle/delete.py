# dept 테이블의 데이터 삭제

import cx_Oracle

try:
    con = cx_Oracle.connect('scott/tiger@localhost:1521/xe')

    cursor = con.cursor()

    no = input('삭제할 부서 번호를 입력 하세요?')

    sql = "delete from dept where deptno = :no"

    cursor.execute(sql, no=no)
    con.commit()

    print('삭제성공')

except Exception as err:
    print(err)
finally:
    con.close()
