import socket

# 查看当前主机名
print('当前主机名称为 : ' + socket.gethostname())

# 根据主机名称获取当前IP
print('当前主机的IP为: ' + socket.gethostbyname(socket.gethostname()))


# 下方代码为获取当前主机IPV4 和IPV6的所有IP地址(所有系统均通用)
addrs = socket.getaddrinfo(socket.gethostname(),None)
print (addrs)
for item in addrs:
    print(item)
    print (item[4][0])

# 仅获取当前IPV4地址
print('当前主机IPV4地址为:' + [item[4][0] for item in addrs if ':' not in item[4][0]][0])

# 同上仅获取当前IPV4地址
for item in addrs:
    if ':' not in item[4][0]:
        print('当前主机IPV4的的顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶顶地址为:' + item[4][0])
        break

hi=[1, 0, 0, '', ('fe80::b541:867b:67d4:78a1', 0, 0, 26)]
print (hi[4][0])


# [(<AddressFamily.AF_INET6: 23>, 0, 0, '', ('fe80::4030:3367:74d8:5c9e', 0, 0, 33)), (<AddressFamily.AF_INET6: 23>, 0, 0, '', ('fe80::d02a:841:a64a:488c', 0, 0, 13)), (<AddressFamily.AF_INET6: 23>, 0, 0, '', ('fe80::6d10:8ff1:1f9e:7ff9', 0, 0, 25)), (<AddressFamily.AF_INET6: 23>, 0, 0, '', ('fe80::b541:867b:67d4:78a1', 0, 0, 26)), (<AddressFamily.AF_INET: 2>, 0, 0, '', ('192.168.56.1', 0)), (<AddressFamily.AF_INET: 2>, 0, 0, '', ('10.235.151.10', 0)), (<AddressFamily.AF_INET: 2>, 0, 0, '', ('192.168.23.1', 0)), (<AddressFamily.AF_INET: 2>, 0, 0, '', ('192.168.94.1', 0))]