#  내장 함수 : print() -> 줄바꿈이 기본

print(1, 2)
print(3, 4)

# 한줄에 2개 이상의 명령을 사용할 경우에는 세미콜론(;)을 붙여야 한다.
print(1, 2);     print(3, 4)

# 줄을 바꾸지 않으려면 print()함수 안에 end=''를 추가하면 된다.
print(1, 2, end=' ');     print(3, 4)
print(1, 2, end='            ');     print(3, 4) # 공백을 추가 하면 그 간격만큼 출력됨

# 값 사이의 간격은 sep='\t' 를 추가
print(1,2,3,4,5)                # 1 2 3 4 5
print(1,2,3,4,5, sep='  ')      # 1  2  3  4  5
print(1,2,3,4,5, sep='\t')      # 1	 2	 3	 4   5
print(1,2,3,4,5, sep='\t\t')    # 1		2		3		4		5
