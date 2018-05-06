import zipfile

final = ""

result = "90052.txt"                                                       # 초기값
while (len(result) != 0):                                                  # 숫자가 안나오면 루프 종료
    if(result == "46145.txt"):                                             # 46145 다음은 값이 없으므로 루프 종료
       break
    File_ = zipfile.ZipFile('C:\\Users\\m3\\Desktop\\channel.zip', 'r')    # 다음경로의 channel.zip파일을 불러온다
    q = File_.getinfo(result).comment                                      # 파일의 코멘트를 불러와 q에 저장
    a = q.decode('utf-8')                                                  # 불러온 코멘트는 바이트형식이라 디코딩 해준다.

    print(a,result)
    final+=a                                                               # 각각 불러온 코멘트를 문자열로 합해준다.

    p = open("C:\\Users\\m3\\Desktop\\channel\\"+result,'r')               # 다음과 같은 경로에 파일을 연다.

    text = p.read()                                                        # 텍스트 파일 내용을 text에 저장

    import re as r

    q = r.compile('[0-9]+')                                                # 내용에서 숫자만 추출

    string = q.findall(text)
    string.append(".txt")                                                  # 숫자뒤에 확장자 ".txt"를 삽입

    result=""
    for i in range(len(string)):                                           # 한번에 대입을 하기 위해 한 문자열로 합치기
        result+=string[i]


print(final)                                                               # 최종적인 문자열을 출력한다.