from urllib import request
from bs4 import BeautifulSoup

class spider:

    def __init__(self):
        self.url = r"http://www.jianshu.com"
        self.header = {"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

    def spider_baidu(self):
        page = request.Request(self.url,headers = self.header)
        page_info = request.urlopen(page).read().decode("utf-8")
        soup = BeautifulSoup(page_info,'html.parser')
        titles = soup.findall('a','title')
        try:
            file = open(r"E:\python\study\study_spider","w")
            for title in titles:
                file.write(title.strings+"\n")

        finally:
            if file:
                file.close()
spider().spider_baidu()