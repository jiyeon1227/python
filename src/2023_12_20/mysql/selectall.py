# contact 테이블의 모든 데이터를 검색

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
    rows = cursor.fetchall()        # 모든 데이터를 구해옴
    print(type(rows))               # 'tuple'
    print(rows)                     # cf. sqlite, oracle은 list로 처리됨

    for r in rows:
        print(r)

except Exception as err:
    print(err)
finally:
    con.close()
