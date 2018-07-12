from urllib import request
from bs4 import BeautifulSoup


class spider:
    def __init__(self):
        self.url = r"http://www.jianshu.com"
        self.header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    def spider_jianshu(self):
        page = request.Request(self.url, headers=self.header)
        page_info = request.urlopen(page).read().decode("utf-8")
        soup = BeautifulSoup(page_info, 'html.parser')
        titles = soup.find_all('a', 'title')
        try:
            file = open(r"E:\python\study\study_spider\spider.txt", "w",encoding = "utf-8")
            for title in titles:
                file.write(str(title)+"\n")

        finally:
            if file:
                file.close()


spider().spider_jianshu()
