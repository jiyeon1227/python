# dept 테이블의 데이터 수정

import cx_Oracle

try:
    con = cx_Oracle.connect('scott/tiger@localhost:1521/xe')
    cursor = con.cursor()

    no = input('부서번호를 입력하세요?')
    name = input('수정할 부서명을 입력하세요?')
    local = input('수정할 지역명을 입력하세요?')

    sql = "update dept set dname=:name, loc=:local where deptno=:no"
    cursor.execute(sql, name=name, local=local, no=no)
    con.commit()
    print('수정 성공')

except Exception as err:
    print(err)
finally:
    con.close()

