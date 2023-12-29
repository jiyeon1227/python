# contact 테이블의 데이터 수정

import pymysql

try:
    con = pymysql.connect(host='localhost',
                          user='jspid',
                          passwd='jsppass',
                          port=3306,
                          db='jsptest',
                          charset='utf8')
    cursor = con.cursor()
    sql = "update contact set phone='1234' where num=1"
    cursor.execute(sql)
    con.commit()
    
    print('수정 성공')

except Exception as err:
    print(err)
finally:
    con.close()