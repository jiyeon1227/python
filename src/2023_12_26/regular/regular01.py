# 정규표현식을 사용하지 않고 주민번호 뒷자리를 * 로 변경

data = """
        park 800905-1049118
        kim  700905-1059119
       """
result=[]
for line in data.split('\n'):           # line = "park 800905-1049118"
 word_result=[]                         # word = "park"

 for word in line.split(' '):           # word = "800905-1049118"
    if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
        word = word[:6]+'-'+'*******'   # word = "800905-*******"
    word_result.append(word)            # word_result=["park","800905-*******"]
 result.append(" ".join(word_result))
print('\n'.join(result))
