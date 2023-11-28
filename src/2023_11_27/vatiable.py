# 변수 : 메모라상에 데이터를 저장하기 위한 기억 공간의 이름
# 변수 만드는 형식 : 변수명 = 값(데이터)

# 정수형 변수
i=10
print("i=",i)
print(type(i)) # type()은 변수가 어떤 자료형인지 확인하는 함수

# 실수형 변수
r = 3.14
print("r=",r)
print(type(r))

# 복소수형 변수
c=3+5j
print("c=",c)
print(type(c))

# 논리형 변수

# 문자형 변수
s1= "파이썬"
s2= "py"
print(type(s1))
print(type(s2))

#리스트
list = ["빨","주","노","초","파","남","보"]
print(list[0])
list[0] = "red"
print("list=",list)
print(type(list))

# 튜플(tuple) -> 원소값 수정 불가
t = {"red","orange","yello","green","blue","navy"}
# t[0] = "빨강" -> tuple은 원소를 수정 할 수 없다.
print(type(t))

# 딕셔너리(dictionary) : {"key" : "value"}
d={"네이버" : "http://www/naver.com"}
print(type(d))