from urllib import request

response = request.Request("http://www.baidu.com")
print(request.urlopen(response).read())
