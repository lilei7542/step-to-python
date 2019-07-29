from urllib.parse import urljoin

# print(urljoin('http://www.baidu.com', 'FAQ.html'))

# print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))


# print(urljoin('http://www.baidu.com', '?category=2#comment'))


# print(urljoin('www.baidu.com#comment', '?category=2'))


from urllib.parse import urlencode

params = {
    "name":"zhaofan",
    "age":23,
}
base_url = "http://www.baidu.com?"

url = base_url+urlencode(params)
print(url)




import urllib.request

response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())



from urllib.parse import urlencode

params = {
    "name":"zhaofan",
    "age":23,
}
base_url = "http://www.baidu.com?"

url = base_url+urlencode(params)
print(url)