# 1차원 배열 슬라이싱

import numpy as np

# 1차원 배열 정의
b1 = np.array([0, 10, 20, 30, 40, 50])

# 배열[시작위치 : 끝위치]:시작위치 ~ 끝위치-1 까지 슬라이싱
# 인덱스 1 ~ 3번 원소를 슬라이싱
print(b1[1:4])              # [10 20 30]

# 배열[시작위치 : ]:시작위치 ~ 끝위치 까지 슬라이싱
# 인덱스 2번 부터 끝까지 슬라이싱
print(b1[2:])               # [20 30 40 50]

# 배열[ : 끝위치]:시작위치 ~ 끝위치-1 까지 슬라이싱
# 처음부터 인덱스 2번 부터 끝까지 슬라이싱
print(b1[:3])               # [ 0 10 20]

# 슬라이싱으로 원소의 값 변경
# 인덱스 2~4번 원소의 값을 [25, 35, 45]로 변경
b1[2:5] = np.array([25, 35, 45])
print(b1)                   # [ 0 10 25 35 45 50]

# 인덱스 3 ~ 5번 원소의 값을 60 으로 변경
b1[3:6] = 60
print(b1)                   # [ 0 10 25 60 60 60]