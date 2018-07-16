from urllib import request
from bs4 import BeautifulSoup
import pymysql


class spider:
    def __init__(self):
        self.url = r"http://www.jianshu.com"
        self.header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        self.db_config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '111111',
            'db': 'pytest',
            'charset': 'utf8'
        }
        self.connction = pymysql.connect(**self.db_config)

    def spider_data_base(self):
        page = request.Request(self.url, headers=self.header)
        page_info = request.urlopen(page).read().decode("utf-8")
        soup = BeautifulSoup(page_info, 'html.parser')
        urls = soup.find_all('a', 'title')
        print(urls)
        try:
            with self.connction.cursor() as cursor:
                sql = 'insert into titles(title,url) value (%s,%s)'
                for u in urls:
                    cursor.execute(sql, (u.string, r'http://www.jianshu.com' + u.attrs['href']))
            self.connction.commit()
        finally:
            self.connction.close()


spider().spider_data_base()
