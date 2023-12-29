# 키보드로 입력한 정보를 dept 테이블에 입력하기

import cx_Oracle

try:
    con = cx_Oracle.connect('scott/tiger@localhost:1521/xe')
    cursor = con.cursor()

    # 키보드로 데이터 입력 받기
    no = int(input('부서번호를 입력하세요?'))
    name = input('부서명을 입력하세요?')
    local = input('지역명을 입력하세요?')

    sql = "insert into dept values(:no, :name, :local)"
    cursor.execute(sql, no=no, name=name, local=local)
    con.commit()
    print('데이터 입력 성공')

except Exception as err:
    print(err)
finally:
    con.close()
