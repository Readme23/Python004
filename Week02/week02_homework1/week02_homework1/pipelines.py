# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter

class Week02Homework1Pipeline:
    dbInfo = {
    'host': 'localhost',
    'prot': '3306',
    'user': 'root',
    'password': 'admin',
    'db': 'maoyan',
    'charset': 'utf8mb4'
    }

    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.charset = dbInfo['utf-8']
        self.sqls = sqls

    def run(self, item, spider):
        conn = pymsql.connect(
            host = self.host,
            prot = self.port,
            user = self.user,
            password = self.password,
            charset = self.charset,
            db = self.db
        )

        name = item['name']
        link = item['link']
        movie_type = item['movie_type']

        # 游标建立的时候就开启了一个隐形的事务
        cur = conn.cursor()
        sql = 'insert into movies values(%s,%s,%s);',(name,link,movie_type)
        cur.execute(sql)
        cur.close
        conn.commit()
        conn.close()