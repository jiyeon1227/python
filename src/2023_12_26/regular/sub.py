# sub() 함수 : 문자열을 치환 해주는 함수
# 형식 : sub(바꿀 문자열, 대상 문자열)

import re

# 정규 표현식 생성
p = re.compile('blue|white|red')

# blue, white, red 라는 문자를 color로 치환
print(p.sub('color', 'blue socks and red shoes'))

# 출력 결과
# color socks and color shoes

# 치환하는 횟수 지정
# blue, white, red 라는 문자를 color로 치환(1번만 치환함)
print(p.sub('color', 'blue socks and red shoes', count=1))

# 출력 결과
# color socks and red shoes