# contact 테이블에 데이터 입력

import pymysql

try:
    # 데이터베이스 접속
    con = pymysql.connect(host='localhost',
                          user='jspid',
                          passwd='jsppass',
                          port=3306,
                          db='jsptest',
                          charset='utf8')

    # 커서 생성
    cursor = con.cursor()

    # SQL문 실행
    sql ="insert into contact(name, phone) values('안화수','010-1111-2222')"

    cursor.execute(sql)
    con.commit()

    print('데이터 입력 성공')

except Exception as err:
    print(err)
finally:
    con.close()

