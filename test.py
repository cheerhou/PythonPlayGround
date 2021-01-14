import requests

url = 'http://www.cntour.cn/'

# 发送get请求
strhtml = requests.get(url)
print(strhtml.text)
