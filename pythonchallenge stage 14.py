from PIL import Image                                   # 이미지 모듈

im = Image.open("C:\\Users\\m3\\Desktop\\wire.png")     # 이미지 파일 열기
print(im.mode)
new_im = Image.new('RGB',[101,100],'white')             # 100x100 크기의 이미지보드 만들기
p=0                                                     # wire.png의 x값을 증가시킬 변수
x,y = 0,0                                             
xy = [[1,0],[0,1],[-1,0],[0,-1]]                        # 사각형으로 그려나갈 좌표 리스트
value = 100                                             # 초기값
i=0
while value!=0:                                         # 값이 0이 될때 까지 루프

    if i>3:                                             # 좌표 리스트가 4이상일 경우 다시 첫번째 리스트로 백
        i -=4
    if value == 100:                                    # 처음 100의 값일 때만 1번 수행
        for k in range(value):
            x += xy[i][0]
            y += xy[i][1]
            new_im.putpixel((x, y), im.getpixel((p, 0)))
            p+=1
        value -=1
        i+=1
        continue
    for j in range(2):                                  # 처음 값을 제외한 나머지 값들은 2번씩 반복
        for k in range(value):                          # value 값만큼 루프를 수행하여 값을 대입
            x += xy[i][0]
            y += xy[i][1]
            new_im.putpixel((x,y), im.getpixel((p, 0)))
            p+=1
        i+=1
        if i > 3:
            i -= 4

    value -=1
new_im.show()                                           # 결과 출력
im.close()