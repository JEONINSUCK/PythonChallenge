import base64
import wave
import array

f = open('C:\\project\\19.txt','rb')
bstring = f.read()
f.close()

print(base64.decodestring(bstring))
f = open('C:\\project\\b19.wav','wb')
f.write(base64.decodestring(bstring))
f.close()

w = wave.open('C:\\project\\b19.wav','rb')
res = wave.open('C:\\project\\new19.wav','wb')
print(w.getnchannels())
print(w.getsampwidth())
print(w.getframerate())

res.setnchannels(w.getnchannels())
res.setsampwidth(w.getsampwidth())
res.setframerate(w.getframerate())

a = array.array('i', base64.decodestring(bstring))
a.byteswap()
res.writeframes(a.tostring())

res.close()
w.close()


