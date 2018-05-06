import urllib.parse
import requests

print("\t-----------------------coding------------------------")

#799번째 값
nothing = str(44827)

sentense = "B"
for i in range(400):
    print("      i          : %d" %i)
    import urllib .request as u                                                             # urllib 모듈을 호출하여 u로 간략화
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="+nothing
    d= u.urlopen(url)                                                                       # 다음과 같은 주소의 url을 서버에 요청 후 내용을 d에 저장
    bstring = (d.read())                                                                    # url의 내용을 읽어 bstring에 저장(내용은 바이트형식)
    string = bstring.decode('utf-8')                                                        # 바이트형식의 내용을 문자열로 바꿔 string에 저장
    # 해당 url에서 쿠기 값만 추출하기
    r = requests.get(url)
    cookie = r.cookies['info']
    sentense+=cookie

    print("This URL String : ",string)

    import re as r                                                                          # 정규화를 위해 re 모듈을 호출
    p = r.compile('[0-9]')                                                                  # 0~9까지 찾는 명령어 입력
    result = ""
    a = p.findall(string)                                                                   # 입력한 명령어로 string에 있는 문자열 검색
    for i in range(len(a)):
        result += (a[i])
    if(len(result) == 0):                                                                   # result 변수에 숫자가 없으면 반복문을 멈춘다.
        break
    print("This URL Number : ", result, "cookie :",cookie)


    nothing = result

    result = result


print("--"*10)
print(sentense)
# sentense 문자열
"""BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%
D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%8
0%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0
%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"""
# url의 형식에 맞는 문장을 디코딩 하기 위해서 16진수로 바꿔줄 urllib.parse 모듈
import urllib.parse
import bz2
# urllib.parse가 특수 문자를 해석하지 못함으로 + 를 띄어쓰기로 대체 후 디코딩
sentense =sentense.replace('+'," ")
sentense = urllib.parse.unquote_to_bytes(sentense)
sentense = bz2.decompress(sentense)

print("="*50)
print(sentense)

# 레오폴드에게 전화를 걸기 위한 xmlrpc.client 모듈
import xmlrpc.client
url = "http://www.pythonchallenge.com/pc/phonebook.php"

sever = xmlrpc.client.ServerProxy(url)
print(sever.phone('Leopold'))

# 해당 페이지에 쿠키 값을 집어넣고 페이지 읽어 들이기
req = urllib.request.Request("http://www.pythonchallenge.com/pc/stuff/violin.php")
req.add_header("cookie","info=the flowers are on their way")
result = urllib.request.urlopen(req)
print(result.read())
