from NetworkRequest import NetworkRequest
from requests_toolbelt import MultipartEncoder
import json

n = NetworkRequest()
n.login("admin001","111111")
token = n.getNowToken()
#处理上传文件
m = MultipartEncoder(
    fields = {
        "_token":token,
        "image":("a.png",open("E:\\python\\study\\file_uploads\\a.png","rb"),"image/png")
    }
)
req = n.post2("/api/tempimage",m,m.content_type)
print(req.content)
fa_logo = json.loads(req.content)["result"]["tmp_path"][18:]

print(fa_logo)
#更新足协基本信息
data = {
    "logo":fa_logo,
    "_token":token,
    "_method":"put",
    "fa_base_id":76
}

req = n.post("fa/update",data)
print(req.text)