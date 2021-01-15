from selenium import webdriver

url = 'http://www.baidu.com/'
path = '/Users/23mofang-hcj/chromeWebDrive/chromedriver'
browser = webdriver.Chrome(executable_path=path)
browser.get(url)
