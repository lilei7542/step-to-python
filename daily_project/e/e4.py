import socket
import ipaddress
a=socket.IP_ADD_MEMBERSHIP
print (a)

b=ipaddress.IPv4Network.hosts
print (b)


c=ipaddress.ip_address('1.1.1.1')
print (c._version)


import socket

# # 方法一
# localIP = socket.gethostbyname(socket.gethostname())
# print ("local ip address: %s"%localIP)

# ipList = socket.gethostbyname_ex(socket.gethostname())


d=socket.gethostname()
e=socket.gethostbyaddr(socket.gethostname())
f=socket.gethostbyaddr('1.1.1.1')
print (f)

# print (d)
# print (e)



import socket

# 方法一
localIP = socket.gethostbyname(socket.gethostname())
print ("local ip address: %s"%localIP)

ipList = socket.gethostbyname_ex(socket.gethostname())

# 循环打印
for i in ipList:
    if i != localIP:
        print ("Other ip address: %s"%i)
