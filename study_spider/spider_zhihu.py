from urllib import request
from bs4 import BeautifulSoup
import re
import time


#抓取图片信息，只能抓取静态的网页
class spider:
    def __init__(self):
        self.url = r"https://www.zhihu.com/question/22918070"
        self.header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    def spider_image_baidu(self):
        page = request.Request(self.url, headers=self.header)
        page_info = request.urlopen(page).read().decode("utf-8")
        soup = BeautifulSoup(page_info, 'html.parser')

        # links = soup.find_all('img', 'origin_image zh-lightbox-thumb lazy',src = re.compile(r'.jpg'))
        links = soup.find_all('img','origin_image zh-lightbox-thumb lazy')
        print(links)
        local_path = r'E:\\python\\study\\study_spider\\pic\\'
        for link in links:
            print(link.attrs["data-actualsrc"])
            request.urlretrieve(link.attrs["data-actualsrc"],local_path + r'%s.jpg' %time.time())


spider().spider_image_baidu()
