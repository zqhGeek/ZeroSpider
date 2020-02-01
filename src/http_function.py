import requests


def http_connect(http_address="http://www.baidu.com"):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Host': 'search.smzdm.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 ',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    try:
        response = requests.get(http_address, headers=headers)
        response.raise_for_status()  # 当返回code不是200的时候会触发异常
        response.encoding = response.apparent_encoding
        return response.text
    except Exception as e:
        print(e)
        return ""
