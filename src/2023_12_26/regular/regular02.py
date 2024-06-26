# 정규표현식을 사용하여 주민번호 뒷자리를 * 로 변경

import re

data = """
        park 800905-1049118
        kim  700905-1059119
       """

# 정규 표현식 생성
pat = re.compile('(\d{6})[-](\d{7})')       # (): 정규표현식을 그룹으로 묶어준다.

# sub( 바꿀 문자열, 대상 문자열 )
# g<그룹명> : 정규표현식의 첫번째 그룹을 참조함 (그룹번호는 1번부터 시작함)
# 주민번호 뒷자리를 * 문자로 변경
print(pat.sub("\g<1>-*******", data))

# 주민번호 앞자리를 * 문자로 변경
print(pat.sub("******-\g<2>", data))