f = open("C:\\Users\\m3\\Desktop\\source.txt",'r')

string = f.read()                   # 어마어마한 길이의 문자열을 텍스트 파일에 저장 후 불러와서 변수  f에 삽입


answer = ""

for i in range(len(string)):
    for j in range(97,123):         # 소문자 알파벳 a ~ z의 아스키 코드 97 ~ 122를 범위로 정함
        if(ord(string[i]) == j):
            answer+=str(string[i])    # 문자열을 한번에 출력하기 위해서 문자를 한개씩  answer 변수에 저장

print("\n\n--------------------------------coding-------------------------------\n\n")
print("pythonchallenge stage 2 answer: %s" %answer)

