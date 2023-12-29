# contact 테이블의 데이터 삭제

import pymysql

try:
    con = pymysql.connect(host='localhost',
                          user='jspid',
                          passwd='jsppass',
                          port=3306,
                          db='jsptest',
                          charset='utf8')
    cursor = con.cursor()

    num = input('삭제할 회원번호를 입력하세요?')
    
    # 데이터 삭제
    sql = 'delete from contact where num = %s'
    cursor.execute(sql, num)
    print('회원 삭제')

    # 모든 데이터 검색
    cursor.execute('select * from contact')
    rows = cursor.fetchall()            # 모든 데이터를 구해옴

    for r in rows:
        print(r)

    # 데이터 갯수 구하기
    cursor.execute('select count(*) from contact')
    count = cursor.fetchone()           # 총 데이터 갯수 구하기    
    for c in count:
        print('총 데이터 갯수:', c,'개')

    con.commit()

except Exception as err:
    print(err)
finally:
    con.close()