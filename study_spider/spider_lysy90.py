import requests
from bs4 import BeautifulSoup

class spider:

    def __init__(self):
        self.url = "http://vip.lysy90store.xyz/cities"
        self.header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    def spider_lysy90(self):
        response = requests.get(self.url,headers = self.header)
        lysy90 = response.content
        print(response.content)
        page = BeautifulSoup(lysy90,'html.parser')
        page_infos = page.find_all('p','hc-2-name')
        print(page_infos)
        for page_info in page_infos:
            print(page_info)

spider().spider_lysy90()