print("\t-----------------------coding------------------------")

nothing = str(8022)                                                                        #799번째 값

for i in range(400):
    print("      i          : %d" %i)
    import urllib .request as u                                                             # urllib 모듈을 호출하여 u로 간략화
    d= u.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nothing)   # 다음과 같은 주소의 url을 서버에 요청 후 내용을 d에 저장
    bstring = (d.read())                                                                    # url의 내용을 읽어 bstring에 저장(내용은 바이트형식)
    string = bstring.decode('utf-8')                                                        # 바이트형식의 내용을 문자열로 바꿔 string에 저장


    print("This URL String : ",string)

    import re as r                                                                          # 정규화를 위해 re 모듈을 호출
    p = r.compile('[0-9]')                                                                  # 0~9까지 찾는 명령어 입력
    result = ""
    a = p.findall(string)                                                                   # 입력한 명령어로 string에 있는 문자열 검색
    for i in range(len(a)):
        result += (a[i])

    result = result

    if(len(result) == 0):                                                                   # result 변수에 숫자가 없으면 반복문을 멈춘다.
        break

    print("This URL Number : ", result)


    nothing = result