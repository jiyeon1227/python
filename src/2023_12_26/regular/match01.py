import re

m1 = re.match('[0-9]', '1234')
print(m1)                           # match='1'
print(m1.group())                   # 1 : 매치된 문자열 반환

m2 = re.match('[0-9]', 'abc')
print(m2)                           # None : 매치되는 문자 없음

m3 = re.match('[0-9]+', '1234')
print(m3)                           # match='1234'
print(m3.group())                   # 1234

# 맨 앞에 공백이 있는 경우
m4 = re.match('[0-9]+', ' 1234')
print(m4)                           # None

# 맨 앞에 공백이 오는 경우에는 \s를 이용해야 한다.
m5 = re.match('\s[0-9]+', ' 1234')
print(m5)                           # match=' 1234'
print(m5.group())                   # 1234

# search()메소드는 문자열 전체를 검색하여 정규식과 매치되는지 검사한다.
m6 = re.search('[0-9]+', ' 1234')
print(m6)                           # match='1234'
print(m6.group())                   # 1234