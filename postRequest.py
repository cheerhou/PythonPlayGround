import requests
import json


def get_translate_data(word=None):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    form_data = {
        'i': word,
        'form': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dic',
        'client': 'fanyideskweb',
        'salt': '16106077982327',
        'sign': 'f6d2f9dbcba877cc6b055df84ad348ef',
        'lts': '1610607798232',
        'bv': '1f12fb36c67fcd2ed7fce620226e3123',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }

    # 发送POST请求
    response = requests.post(url, data=form_data)
    print(response.text)
    # JSON转字典
    content = json.loads(response.text)
    print(content['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    get_translate_data('我爱学习，学习使人进步')
