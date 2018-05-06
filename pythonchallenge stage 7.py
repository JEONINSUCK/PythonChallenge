from PIL import Image                                       # 이미지 수정 모듈 임폴트

im = Image.open('C:\\Users\\m3\\Desktop\\oxygen.jpeg')
pix = []
for i in range(0,606,7):                                    # 이미지 중간의 암호의 픽셀정보를 pix리스트에 입력
    pix.append(im.getpixel((i,45)))                         # 47은 이미지 중간 흑백 암호 y값

print(pix)

string = ""
for j in pix:                                               # 픽셀정보를 아스키코드로 변환
    string += chr(j[0])

print(string)                                               # 아스키코드로 변환한 힌트 출력

import re                                                   # 정규화 모듈 임포트

q = re.compile('[0-9]+')                                    # 힌트에서 숫자만 뽑아오는 명령어

result = q.findall(string)                                  # 숫자만 뽑아서 리스트화


answer = ""
for i in result:                                            # 뽑아온 숫자들 아스키코드 변환
    answer += chr(int(i))
print("--------------------------\t")
print("answer is : " ,answer)                               # 정답 출력
