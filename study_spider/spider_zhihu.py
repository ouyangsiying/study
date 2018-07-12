from urllib import request
from bs4 import BeautifulSoup
import re
import time


class spider:
    def __init__(self):
        self.url = r"http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%B7%E7%BE%B0&fr=ala&ala=1&alatpl=adress&pos=0&hs=2&xthttps=000000"
        self.header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    def spider_zhihu(self):
        page = request.Request(self.url, headers=self.header)
        page_info = request.urlopen(page).read().decode("utf-8")
        soup = BeautifulSoup(page_info, 'html.parser')

        # links = soup.find_all('img', 'origin_image zh-lightbox-thumb lazy',src = re.compile(r'.jpg'))
        links = soup.find_all('img','main_img img-hover')
        print(links)
        local_path = r'E:\\python\\study\\study_spider\\pic\\'
        for link in links:
            print(link.attrs["data-imgurl"])
            request.urlretrieve(link.attrs["data-imgurl"],local_path + r'%s.jpg' %time.time())


spider().spider_zhihu()
