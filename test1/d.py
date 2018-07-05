import requests
from requests_toolbelt import MultipartEncoder
from NetworkRequest import NetworkRequest
import re

headers ={
    "Accept": "application / json, text / javascript, * / *; q = 0.01",
    "User - Agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64;rv:61.0) Gecko / 20100101Firefox / 61.0",
    "X - Requested - With": "XMLHttpRequest"
}

n = NetworkRequest()
token = n.getNowToken()
s = requests.session()
# print(s.cookies)
c = requests.cookies.RequestsCookieJar()
c.set("laravel_session","eyJpdiI6Ikd5XC90RThrczIweE9CUVhwbSttU3NnPT0iLCJ2YWx1ZSI6InJadFpITVFzZ0VjcnVzTzN4QXMzdGIyalBuVDc1S250aTU3eVREb1AyeGFpUGhVYnRpUUVQUFwvYWg1QXRJcmtcL21pWUVRNkJCRzUxS1NvTGtmVDVPNmc9PSIsIm1hYyI6IjQwM2RlNzA4MzczZjQ0MDU0MGMxMmEzZmIxMWZmMTBiZWQ5NWNlMDgwNzBmOWE2MWE1MDQyYjY1MDk2ZTY1NDAifQ%3D%3D")
s.cookies.update(c)

m = MultipartEncoder(
    fields = {
        "_token":"b7h9Kqe36UvrgkFgU5H1VwpHeHD2wLnmGzrC9ipV",
        "image":("a.png",open("E:\\python\\login_bug\\a.png","rb"),"image/png")
    }
)
headers['Content-Type'] = m.content_type
req = s.post("http://vip.lysy90store.xyz/api/tempimage", data=m, headers=headers )
print(req.content)
