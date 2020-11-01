# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql as pq

class DoubanMoviePipeline(object):
    def __init__(self):
        self.conn = pq.connect(
            host='localhost',
            user='root',
            passwd='',
            db='douban',
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        title = item['title']
        short_evaluate = item['short_evaluate']
        star = item['star']

        sql = "insert into movies(movie_title, movie_evaluate, movie_star) values (%s, %s, %s)"
        
        self.cur.execute(sql, (title, short_evaluate, star))
        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()