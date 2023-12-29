# 주민번호 형식 검사

import re

# 주민번호 정규식 생성
p = re.compile('(\d{6})-(\d{7})')

num = input('주민번호를 입력하세요? (900101-1234567) ')
# num = '100000-2000000'
print(p.search(num))                # match='100000-2000000'

if p.search(num) != None:
    print('올바른 주민번호 형식입니다.')
else:
    print('올바른 주민번호 형식이 아닙니다.')

