# user 테이블에 데이터 입력

import sqlite3

try:
    # 데이터베이스 접속
    con = sqlite3.connect('naverDB')

    cursor = con.cursor()
    
    while True:
        data1 = input('사용자 ID?')
        if data1 == '':
            break
        data2 = input('사용자 이름?')
        data3 = input('사용자 Email?')
        data4 = input('사용자 생년월일?')

        # sql = "insert into user values('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + "')"
        sql = "insert into user values(?, ?, ?, ?)"
        cursor.execute(sql, (data1,data2,data3,data4))

    con.commit()

except Exception as err:
    print(err)
    print('데이터 베이스 연결 실패')
finally:
    con.close()