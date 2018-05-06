f = open("C:\\Users\\m3\\Desktop\\source2.txt",'r')

source = f.read()

answer = []                                    # 결과의 문자열을 할당할 배열

for i in range(len(source)-8):                  # 문자열의 범위만큼 반복문을 돌지만 마지막 범위를 생각해서 6을 빼준다
    inspect = []                                # 뽑아낸 7자리 문자가 대문자인지 소문자인지 구분할 배열
    test = []                                   # source 에서 7자리씩 문자열을 뽑아서 저장할 배열 변수
    for j in range(9):                          # 문자열 7자리를 뽑는 반복문
        test.append(source[i+j])

    for k in range(len(test)):                  # 알파벳이 대문자면 True를 소문자면 False를 inspect배열에 저장
        inspect.append(test[k].isupper())

    if(inspect[0] == False
        and inspect[1] == True                       # 7자리 문자열 중에 가운데 알파벳만 소문자일 경우
        and inspect[2] == True
        and inspect[3] == True
        and inspect[4] == False
        and inspect[5] == True
        and inspect[6] == True
        and inspect[7] == True
        and inspect[8] == False
       ):

         answer.append(test[4])                    # 결과물들 중에 가운데 소문자들만 뽑아서 answer배열에 중첩
print(answer)
for i in range(len(answer)):
    if(answer[i] == " "):
        answer[i].remove
        continue
    print(answer[i])