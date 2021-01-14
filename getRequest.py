import re

import requests
from bs4 import BeautifulSoup

url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, 'lxml')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a')
print(data)
for item in data:
    result = {
        'title': item.get_text(),  # 因为在tag a里面，需要用get_text来提取
        'link': item.get('href'),  # 提取 href属性
        'ID': re.findall('\d+', item.get('href'))
    }
    print(result)
