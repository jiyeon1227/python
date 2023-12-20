# 과제. 다음과 같은 내용의 파일 abc.txt 가 있다.
#         AAA
#         BBB
#         CCC
#         DDD
#         EEE
#
#        이 파일의 내용을 다음과 같이 역순으로 바꾸어 result.txt로 저장 하세요?
#        EEE
#        DDD
#        CCC
#        BBB
#        AAA

with open('abc.txt', 'r') as f:
    lines = f.readlines()
    print(lines)                # ['AAA\n', 'BBB\n', 'CCC\n', 'DDD\n', 'EEE']

lines.reverse()
print(lines)                    # ['EEE', 'DDD\n', 'CCC\n', 'BBB\n', 'AAA\n']

with open('result.txt', 'w') as f:
    for line in lines:
        line = line.strip()     # 줄바꿈 문자(공백) 제거
        f.write(line+'\n')
