# coding :utf8
import os
import time
from urllib import request
from urllib import error
import chardet
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


def proxy_http_connect():
    # 这是代理IP
    url = "http://www.baidu.com"
    # 代理地址
    proxy = {'http': '124.205.155.151:9090'}
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    # 创建Opener
    opener = request.build_opener(proxy_support)
    # 添加User Angent
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # 安装OPener
    request.install_opener(opener)
    try:
        # response = opener.open(url)
        response = request.urlopen(url)
        print("geturl打印信息：%s" % (response.geturl()))
        print('**********************************************')
        print("info打印信息：%s" % (response.info()))
        print('**********************************************')
        print("getcode打印信息：%s" % (response.getcode()))
        html = response.read()
        html = html.decode("utf-8")
        print(html)
    except error.URLError as e:
        if type(e) == error.URLError:
            print("URL错误" + str(e))
        if type(e) == error.HTTPError:
            print("HTTP错误" + str(e))


def http_connect(http_address="http://www.baidu.com"):
    req = request.Request(http_address)
    # 传入headers
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
    try:
        response = request.urlopen(req)
        print("geturl打印信息：%s" % (response.geturl()))
        print('**********************************************')
        print("info打印信息：%s" % (response.info()))
        print('**********************************************')
        print("getcode打印信息：%s" % (response.getcode()))
        print('**********************************************')
        html = response.read()
        charset = chardet.detect(html)
        print("charset编码格式：%s" % (charset["encoding"]))
        print('**********************************************')
        if charset["encoding"].find("2312") > 0:
            html = html.decode("gb18030")
        else:
            html = html.decode(charset["encoding"])
        return html
    except error.URLError as e:
        if type(e) == error.URLError:
            print("URL错误" + str(e))
        if type(e) == error.HTTPError:
            print("HTTP错误" + str(e))
        return None


# def cookie_login():

def beautifulsoup_spider():
    download_html = http_connect("http://www.biqukan.com/1_1094/5403177.html")
    soup_texts = BeautifulSoup(download_html, 'lxml')
    texts = soup_texts.find_all(id='content', class_='showtxt')
    soup_text = BeautifulSoup(str(texts), 'lxml')
    # 将\xa0无法解码的字符删除
    return soup_text.div.text


# if __name__ == "__main__":
#     # http_connect("https://www.163.com/")
#
#     # 创建txt文件
#     path = "一念永恒.txt"
#     with open(path, 'a', encoding='utf-8', newline='') as f:
#         f.write(beautifulsoup_spider())
def down_girl(path, girl_id):
    try:
        downloadHtml = http_connect("http://date.jobbole.com/" + girl_id + "/")
        soupTexts = BeautifulSoup(downloadHtml, 'lxml')
        textsFind = soupTexts.find(class_="p-entry")
        textsTitle = soupTexts.find(class_="p-tit-single")
        if str(textsTitle.text).find("脱单") > 0:
            print("已脱单")
            return None
        filePath = path + "/" + str(textsTitle.text)
        if str(textsTitle.text) not in os.listdir(path):
            os.makedirs(filePath)
        tagFind = BeautifulSoup(str(textsFind), 'lxml')
        girlAttribute = str(tagFind.p).replace("\n", "").replace("<p>", "").replace("</p>", "").replace("<br/>", "\n")
        with open(filePath + "/" + "信息卡.txt", 'w', encoding='utf-8', newline='') as f:
            f.write(girlAttribute)
        attributeList = girlAttribute.split("\n")
        print(attributeList[0])
        print(attributeList[3])
        print(attributeList[4])
        print(attributeList[7])
        if str(attributeList[len(attributeList) - 2]).find("http") > 0:
            urlretrieve(str(attributeList[len(attributeList) - 2])[
                        attributeList[len(attributeList) - 2].index("http"):attributeList[len(attributeList) - 2].index(
                            "jpg") + 3], filePath + "/" + "01.jpg")
        if str(attributeList[len(attributeList) - 1]).find("http") > 0:
            urlretrieve(str(attributeList[len(attributeList) - 1])[
                        attributeList[len(attributeList) - 1].index("http"):attributeList[len(attributeList) - 1].index(
                            "jpg") + 3], filePath + "/" + "02.jpg")
    except Exception as e:
        print("错误" + e)
        pass


if __name__ == "__main__":
    download_html = http_connect("http://date.jobbole.com/")
    soup_texts = BeautifulSoup(download_html, 'lxml')
    numberList = []
    if "收集器" not in os.listdir("../"):
        os.makedirs("../收集器")
        pass
    for media in soup_texts.find_all(class_="media"):
        try:
            id_ = BeautifulSoup(str(media), 'lxml').html.body.li.a["data-post-id"]
            numberList.append(id_)
            print(id_)
        except KeyError:
            pass
    for girl in numberList:
        down_girl("../收集器", girl)
        time.sleep(1)
    # for target_id in numberList:
    # for line in soup_texts.
