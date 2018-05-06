from PIL import Image

im = Image.open("C:\\mozart.gif")
# 새 그림판 생성
new = Image.new('RGB',(640,480),'white')

# 1줄에 1개의 선이 있었으므로 1줄씩 루프
for y in range(480):
# 1줄의 픽셀값을 저장시킬 리스트
    row = []
# 루프를 돌며 1줄의 픽셀 값을 모두 리스트에 삽입
    for x in range(640):
        row.append(im.getpixel((x,y)))
# 각 줄에서 필셀값이 195(빨강색)인 값을 찾고 그 위치로부터 픽셀값 재배치
    for i in range(len(row)):
        if row[i] == 195:
            change = row[i:] + row[:i]
            for j in range(len(change)):
                new.putpixel((j,y),change[j])
            break
new.show()