# 키보드로 입력한 정보를 contact 테이블에 저장

import pymysql

try:
    con = pymysql.connect(host='localhost',
                          user='jspid',
                          passwd='jsppass',
                          port=3306,
                          db='jsptest',
                          charset='utf8')

    cursor = con.cursor()

    name = input('이름을 입력하세요?')
    phone = input('전화번호를 입력하세요?')

    cursor.execute("insert into contact(name, phone) values(%s, %s)",(name, phone))

    con.commit()
    
    print('입력 성공')

except Exception as err:
    print(err)
finally:
    con.close()

