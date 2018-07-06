from NetworkRequest import NetworkRequest
from requests_toolbelt import MultipartEncoder

n = NetworkRequest()
n.login("admin001","111111")
token = n.getNowToken()

m = MultipartEncoder(
    fields = {
        "_token":token,
        "image":("a.png",open("./file_uploads/a.png","rb"),"image/png")
    }
)
req = n.post2("/api/tempimage",m,m.content_type)
print(req.content)
# data = {
#     "logo":"2018-07-06_10.34.48-a49a34942884d1270da373eb44aea31e.jpg",
#     "_token":token,
#     "_method":"put",
#     "fa_base_id":76
# }
#
# req = n.post("fa/update",data)
# print(req.text)