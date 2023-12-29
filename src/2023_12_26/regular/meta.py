# 메타문자

import re

# 문자 클래스 : [ ]
# [abc] : a, b, c 중 한개의 문자라도 있으면 매치
# 정규 표현식
p1 = re.compile('[abc]')

print(p1.match('a'))                # match='a'
print(p1.match('before'))           # match='b'
print(p1.match('dude'))             # None

p = re.match('[abc]', 'a')          # match='a'
print(p)


# dot : .
# a.b : a와 b사이에 줄바꿈 문자를 제외한 어떤 문자가 들어가도 모두 매치
p2 = re.compile('a.b')

print(p2.match('aab'))          # match='aab'
print(p2.match('a0b'))          # match='a0b'
print(p2.match('abc'))          # None


# 반복 : *
# ca*t : * 문자 바로 앞에 있는 a가 0번 이상 반복되면 매치
p3 = re.compile('ca*t')

print(p3.match('ct'))           # match='ct'
print(p3.match('cat'))          # match='cat'
print(p3.match('caaat'))        # match='caaat'


# 반복 : +
# + 는 최소 1번 이상 반복될때 사용한다.
# ca+t : +문자 바로 앞에 있는 a가 1번 이상 반복되면 매치
p4 = re.compile('ca+t')

print(p4.match('ca'))           # None
print(p4.match('cat'))          # match='cat'
print(p4.match('caaat'))        # match='caaat'


# 반복 : {m}
# ca{2}t : a가 2번 반복되면 매치
p5 = re.compile('ca{2}t')

print(p5.match('cat'))          # None
print(p5.match('caat'))         # match='caat'


# 반복 : {m, n}
# ca{2, 5}t : a가 2~5회 반복되면 매치
p6 = re.compile('ca{2,5}t')

print(p6.match('cat'))          # None
print(p6.match('caat'))         # match='caat'
print(p6.match('caaaaat'))      # match='caaaaat'


# 반복 : ?
# ? 메타문자가 의미하는 것은 {0,1} 이다.
# ab?c : a가 0~1번 사용되면 매치
p7 = re.compile('ab?c')

print(p7.match('ac'))           # match='ac'
print(p7.match('abc'))          # match='abc'