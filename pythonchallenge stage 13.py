import xmlrpc.client
url = "http://www.pythonchallenge.com/pc/phonebook.php"

sever = xmlrpc.client.ServerProxy(url)

print(sever.system.listMethods())
print(sever.system.methodHelp('phone'))
print(sever.system.methodSignature('phone'))
print(sever.phone('Bert'))
