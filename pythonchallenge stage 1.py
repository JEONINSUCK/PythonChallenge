example = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print("%s\n\n\n" %example)  # 문제 한번 출력
print("---------------------------CODING-------------------------------")
# 코딩 스타트

result = list(range(203))
for i in range(len(example)):
    if(ord(example[i])>=97 and ord(example[i])<=120):   # 아스키코드 소문자의 범위만 값 변환
        result[i] = chr(ord(example[i]) +2)
    elif(example[i] == "y"):                            # y일 경우 a로 순회
        result[i] = "a"
    elif (example[i] == "z"):                           # z일 경우 b로 순회
        result[i] = "b"
    else:
        result[i] = example[i]                          # 아스키코드 소문자 범위를 제외하고는 값 유지
answer = []
string= "map"
temp =""
for i in range(len(result)):
    temp+=result[i]
print(temp)

for i in range(3):
    answer.append(chr(ord(string[i]) +2))

print("----------------------------answer------------------------------")
print("pythonchalleng stage 1 answer: ")
print(answer)