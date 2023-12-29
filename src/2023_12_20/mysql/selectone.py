# contact 테이블의 데이터 1개 검색

import pymysql

try:
    con = pymysql.connect(host='localhost',
                          user='jspid',
                          passwd='jsppass',
                          port=3306,
                          db='jsptest',
                          charset='utf8')

    cursor = con.cursor()

    cursor.execute('select * from contact')

    row = cursor.fetchone()         # 데이터 1개를 구해옴
    print(type(row))                # 'tuple'
    print(row)                      # (1, '안화수', '010-1111-2222')

    for r in row:
        print(r)

except Exception as err:
    print(err)
finally:
    con.close()