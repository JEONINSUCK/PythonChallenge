# 확장자가 gz로 압축된 파일을 풀어주는 모듈
import gzip
# 차이점을 비교해줄 모듈
import difflib
gf = gzip.open("C:\\Project\\deltas.gz")
string_one = []
string_two = []

# 비슷한 두 문장을 각각의 배열에 넣어준다.
for i in gf:
    i = i.decode()
    string_one.append(i[:53])
    string_two.append(i[56:].replace("\n",""))

#print(string_one)
#print(string_two)

# 두 배열의 차이를 보여줄 difflib.Differ()함수를 이용해서 com_string에 저장
com_string = list(difflib.Differ().compare(string_one,string_two))

print(com_string)

# 위 함수를 이용하면 +,- 그리고 공백이 붙은 문장들로 나눠지는데 각각을 사진으로 나눠서 저장할 파일 생성
new1 = open("C:\\Users\\m3\\Desktop\\Plus.jpg",'wb')
new2 = open("C:\\Users\\m3\\Desktop\\Minus.jpg",'wb')
new3 = open("C:\\Users\\m3\\Desktop\\Space.jpg",'wb')

DistriString_plus = []
DistriString_minus = []
DistriString_space = []

# 각 문장의 접두사(+,-,공백)을 제거하고 10진수로 바꾼 뒤 바이트로 다시 변환하여 각각의 파일에 쓴다.
for i in com_string:
    sen = i[2:].split()
    temp = []
    for j in sen:
         temp.append(int(j,16))
    sen = bytes(temp)
    if (i[0]=="+"):
        new1.write(sen)
    elif (i[0]=="-"):
        new2.write(sen)
    else:
        new3.write(sen)


