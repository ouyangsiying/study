import requests
import re

headers ={
    "Accept": "application / json, text / javascript, * / *; q = 0.01",
    "User - Agent": "Mozilla / 5.0(WindowsNT10.0;Win64;x64;rv:61.0) Gecko / 20100101Firefox / 61.0",
    "X - Requested - With": "XMLHttpRequest"
}


s = requests.session()
# print(s.cookies)
c = requests.cookies.RequestsCookieJar()
c.set("laravel_session","eyJpdiI6IkpKS1ZnQkxTVjBGM0ZQUXJHdnF6UXc9PSIsInZhbHVlIjoidm81bHFyRkVlb1p6a0NaTFwvYmNnelV2NklFNWRzQ0FuRDRaWkxSKzdFemNXNnNXcTRRUDYxcklwOERvQ2JtYlk4SUVoM3Zja1VGSCtTU0Exd0RKU01nPT0iLCJtYWMiOiI2OWI1YjY0NWM4ODNiZGIwMDM5OWRmNDY5OGU0OTQ1YTYwMGE1YTcxOWE5M2JjOTBhNjBhMGMwZGNjNzc4Nzk2In0%3D")
s.cookies.update(c)
#发布文章
data = {
   "_token":"TA3QY9tfVlABLOI2joiaPf514mb8J1yRfwS29V3h",
    "fa_base_id":76,
    "is_public":1,
    "tag":1,
    "title":"我是测试6",
    "is_announcement":0 ,
    "show_time":"2018-07-06 16:25:35",
    "title_page":"2018-07-04_14.26.29-f45a98893db7a32a81ca09e65d3b1e06.jpg",
    "content":"测试2222"
}
r = s.post(url = "http://vip.lysy90store.xyz/story" ,data= data,headers = headers)
r_json = r.json()
# print(r_json)
#获取文章id
story_id1 = r_json["result"]["story_id"]
print(story_id1)
#删除文章

data1 ={
    "_token": "TA3QY9tfVlABLOI2joiaPf514mb8J1yRfwS29V3h",
    "_method":"delete",
    "story_id":story_id1
}
r2 = s.post(url = "http://vip.lysy90store.xyz/story" ,data= data1,headers = headers)
print(r2.text)
