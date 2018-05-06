from PIL import Image

f = open("C:\\Users\\m3\\Desktop\\evil2.gfx",'rb')
bstring = f.read()
for i in range(5):
    of =open("C:\\Users\\m3\\Desktop\\%d.jpg"%(i+1),'wb')
    of.write(bstring[i::5])

