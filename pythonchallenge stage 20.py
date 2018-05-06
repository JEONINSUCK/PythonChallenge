from http import client
import re
import requests
import urllib.request
base64_login = 'YnV0dGVyOmZseQ=='
headers = {"Authorization": "Basic %s" % base64_login}
conn = client.HTTPConnection("www.pythonchallenge.com")

"""for n in range(30202, 40000):
    headers["Range"] = "bytes=%s-%s" % (n, n + 1)
    conn.request("GET", "/pc/hex/unreal.jpg", "", headers)
    response = conn.getresponse()
    data = response.read()
    print(response.headers)
    if data:
        print(data)"""

import urllib.request, base64

request = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
cred = base64.b64encode(b"butter:fly")
request.add_header("Authorization", "Basic %s" % cred.decode())
print(request.headers)
# {'Authorization': 'Basic YnV0dGVyOmZseQ=='}

response = urllib.request.urlopen(request)


pattern = re.compile('bytes (\d+)-(\d+)/(\d+)')
content_range = response.headers['content-range']
(start, end, length) = pattern.search(content_range).groups()
request.headers['Range'] = 'bytes=%i-' % (int(end) + 1)
response = urllib.request.urlopen(request)
print(response.headers)

print(response.read().decode())


request.headers['Range'] = 'bytes=1152983631-'
response = urllib.request.urlopen(request)
print(response.headers)

zipfile = response.read()

f = open("C:\\Users\\m3\\Desktop\\stage20.zip",'wb')
f.write(zipfile)