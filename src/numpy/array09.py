# 1차원 배열의 인덱싱

import numpy as np

# 1차원 배열 정의
a1 = np.array([0, 10, 20, 30, 40, 50])
print(a1)                   # [ 0 10 20 30 40 50]

# index 번호 1번 위치의 원소
print(a1[1])                # 10

# index 번호 4번 위치의 원소
print(a1[4])                # 40

# index 번호 5번 위치의 원소값 50 -> 70으로 수정
a1[5] = 70
print(a1[5])                # 70

# 1차원 배열에서 여러개의 원소 구하기
print(a1[[1,3,4]])          # [10 30 40]

