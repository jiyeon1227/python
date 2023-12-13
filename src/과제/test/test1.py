jumin = input("주민번호 13자리를 입력하세요")

if len(jumin) != 13:
    print("13자리를 입력하세요")
elif jumin[6] == "1" or jumin[6] == "3":
    print("남자")
elif jumin[6] == "2" or jumin[6] == "4":
    print("여자")
else:
    print("입력을 확인해주세요.")