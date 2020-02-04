import threading
from bs4 import BeautifulSoup
from src.http_function import http_connect
import re
from src.db_function import DB
import time
import tkinter as tk


class KeyWorkSpider(threading.Thread):
    SQL_HOST = 'localhost'
    SQL_USER = 'root'
    SQL_PASSWORD = '123456'
    SQL_DB = 'smzdm'
    mStopWorking = False

    def __init__(self, key_work, sleep_time):
        self.KeyWork = key_work
        self.SleepTime = sleep_time

    def start_work(self, timer):
        with DB(host=self.SQL_HOST, user=self.SQL_USER, password=self.SQL_PASSWORD, db=self.SQL_DB) as db:
            # 使用预处理语句创建表
            sql = """CREATE TABLE IF NOT EXISTS COMMODITY(
                 ID  VARCHAR (20) NOT NULL PRIMARY KEY ,
                 COMMODITY_TYPE  VARCHAR (20),
                 TITLE VARCHAR (100),  
                 URL VARCHAR (100),
                 IMG VARCHAR (100) )"""
            db.execute(sql)
        self.mStopWorking = False
        number = self.SleepTime
        while self.mStopWorking is not True:
            if isinstance(timer, tk.Label):
                timer['text'] = str(number)
            time.sleep(1)
            number -= 1
            if int(number) == 0:
                print('搜刮关注对象' + self.KeyWork)
                html = http_connect("https://search.smzdm.com/?c=home&s=%s&order=time&v=b" % self.KeyWork)
                self.get_target_detail(html)
                number = self.SleepTime

    def stop_work(self):
        self.mStopWorking = True

    def get_target_detail(self, html):
        if str(html) != "":
            soup = BeautifulSoup(html, "lxml")
            for li in soup.find_all('li', class_='feed-row-wide'):
                commodity_type = li.find(class_='z-feed-img').span.text
                img = "https:" + li.find(class_='z-feed-img').find('img').attrs['src']
                content = li.find(class_='feed-block-title')
                title = content.a['title']
                url = None
                if str(content.a['href']).find("https:") >= 0:
                    url = content.a['href']
                else:
                    url = "https:" + content.a['href']
                pattern = re.compile(r"pageid':'.*", re.S)  # 匹配ID
                # 匹配所有符合条件的内容
                ID = re.search(r"[1-9]\d*", re.search(pattern, content.a['onclick']).group()).group()
                with DB(host=self.SQL_HOST, user=self.SQL_USER, password=self.SQL_PASSWORD, db=self.SQL_DB) as db:
                    # SQL 插入语句
                    search_sql = "SELECT * FROM COMMODITY WHERE ID = %s" % ID
                    db.execute(search_sql)
                    if len(db.fetchall()) > 0:
                        continue
                    insert_sql = "INSERT INTO COMMODITY(ID,COMMODITY_TYPE, TITLE, URL, IMG)VALUES ( '%s','%s','%s','%s','%s')" \
                                 % (ID, commodity_type, title, url, img)
                    print('类型：' + commodity_type + ' ID：' + ID + ' 标题:' + title + ' 地址:' + url + ' 图片:' + img)
                    db.execute(insert_sql)
