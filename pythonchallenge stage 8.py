un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'     # 문자열을 바이트형식으로 바꿈
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'                    # 문자열을 바이트형식으로 바꿈

import bz2 as b

print("un 값 : ",b.decompress(un))         # 바이트형식의 문자열을 압축해제
print("pw 값 : ",b.decompress(pw))         # 바이트형식의 문자열을 압축해제

