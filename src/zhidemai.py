import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

from src.http_function import http_connect
import re

def get_target_detail(html):
    if str(html) != "":
        doc = pq(html)
        soup = BeautifulSoup(html, "lxml")
        for li in soup.find_all('li', class_='feed-row-wide'):
            type = li.find(class_='z-feed-img').span.text
            img  = "https:"+li.find(class_='z-feed-img').find('img').attrs['src']
            content = li.find(class_='feed-block-title')
            title = content.a['title']
            url = content.a['href']
            pattern = re.compile(r"pageid':'.*", re.S)  # 匹配ID
            # 匹配所有符合条件的内容
            id = re.search(pattern, content.a['onclick'])
            search = re.search(r"[1-9]\d*", id.group())
            print('类型：'+type+' ID：'+search.group()+' 标题:'+title+' 地址:'+url+' 图片:'+img)


if __name__ == '__main__':
    html = http_connect("https://search.smzdm.com/?c=home&s=口罩&order=time&v=b")
    get_target_detail(html)
    # response = requests.get("http://www.baidu.com")
    # print(response.status_code)
    # print(response.encoding)
    # response.encoding = response.apparent_encoding
    # print(response.text)
    # print(response.apparent_encoding)
