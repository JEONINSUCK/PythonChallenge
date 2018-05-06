from PIL import Image                                       # 이미지 모듈소환

im = Image.open("C:\\Users\\m3\\Desktop\\cave.jpg",'r')

# 이미지를 분류해서 출력할 그림판 만들기
odd_image = Image.new("RGB",(640,480))
even_image = Image.new("RGB",(640,480))

# I값과 J값을 더했을때 짝수이면 EVEN그림판에 그리고 ODD그림판에 그리기
for i in range(640):
    for j in range(480):
        if ((i+j)%2 ==0):
            even_image.putpixel((i,j),im.getpixel((i,j)))
        else:
            odd_image.putpixel((i, j), im.getpixel((i, j)))

# 각 그림판 화면에 출력
odd_image.show()
even_image.show()

