import re

s = """
    park 010-9999-9988
    kim 010-9909-7789
    lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}") #()로 그룹을 묶음
result = pat.sub("\g<1>-####", s) #묶은 그룹 번호는  g<1>로 시작됨

print(result)