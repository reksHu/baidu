# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
# import pandas
import logging
import sqlite3
class BaiduPipeline(object):
    def __init__(self):
        #self.f = open('blog.json','w')
        self.conn=sqlite3.connect('cnblogs.db')
        self.c=self.conn.cursor()
        # sqlStr="CREATE TABLE blogs(Id integer primary key AUTOINCREMENT, title text,titleLink char(500),suggestNum char(300),content text,author char(500),publishDate char(500))"
        # self.c.execute(sqlStr)
        # self.conn.commit()

        # pass
    def process_item(self, item, spider):
        #content = json.dumps(dict(item),ensure_ascii=False) +",\n"
        # self.f.write(content)
        # print('data exstrap')
        # print(item["title"])
        # title=item["title"]
        # titleLink=item["titleLink"]
        # suggestNum = item['suggestNum']
        # content = item['content']
        # author = item['author']
        # publishDate = item['publishDate']
        # print(type(titleLink))
        # result = self.duplidateHandle(titleLink)
        # if result == False:
        #     sqlStr = "insert into blogs(title,titleLink,suggestNum,content,author,publishDate) values(?,?,?,?,?,?)"
        #     self.c.execute(sqlStr, (title, titleLink, suggestNum, content, author, publishDate))
        #     self.conn.commit()
        # else:
        #     logging.warning('duplidateHandle return true')
        return item

    def close_spider(self, spider):
        self.conn.close()
        # pass

    def duplidateHandle(self, titleLink):
        sqlStr="select count(*) from blogs where titleLink = :link"
        print(sqlStr,titleLink)
        data = self.c.execute(sqlStr,{"link": titleLink})
        # logging.warning(sqlStr)
        # print(type(titleLink))
        # print(type(sqlStr))
        for d in data:
            if d[0] > 0:
                return True
            else:
                return False
