from NetworkRequest import NetworkRequest
from requests_toolbelt import MultipartEncoder

n = NetworkRequest()
n.login("admin001","111111")
token = n.getNowToken()

m = MultipartEncoder(
    fields = {
        "_token":token,
        "image":("a.png",open("E:\\python\\login_bug\\a.png","rb"),"image/png")
    }
)
req = n.post2("/api/tempimage",m,m.content_type)
print(req.content)
