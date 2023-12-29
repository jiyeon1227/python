# python - mongodb 연동 예제

import pymongo

con = pymongo.MongoClient('localhost',27017) # 서버가 구동 되어 있어야 동작함

# 데이터베이스 생성 : testdb
db = con.testdb

# collection 생성 : collect
collect = db.collect

# document 생성 : {'key':'value'}
doc1 = {'empno': '10001', 'name': 'hong', 'phone': '010-111-111', 'age': 35}
doc2 = {'empno': '10002', 'name': 'lee', 'age': 45}
doc3 = {'empno': '10003', 'name': 'yoo', 'phone': '010-222-222', 'age': 25}

# collection에 문서 추가
db.collect.insert(doc1)
db.collect.insert(doc2)
db.collect.insert(doc3)

# 전체 문서 조회
print('전체 문서 검색')
result1 = db.collect.find()
for r in result1:
    print(r)

# 조건검색
print('조건검색')
result2 = db.collect.find({'age':{'$gte':30}})  # age가 30보다 크거나 같다.
for r in result2:
    print(r)

# 문서 수정
# empno가 10001인 경우에 name을 'hong' 에서 'kim'으로 수정
db.collect.update({'empno':'10001'},{'$set':{'name':'kim'}}, multi=True)

# 수정 결과 확인
print('문서 수정 결과 확인')
result3 = db.collect.find()
for r in result3:
    print(r)

# 문서 삭제
# empno가 10002인 데이터 삭제
db.collect.remove({'empno':'10002'})

# 문서 삭제후 검색
print('문서 삭제 결과 확인')
result4 = db.collect.find()
for r in result4:
    print(r)

# 컬렉션 제거
# db.collect.drop()
