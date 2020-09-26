# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from maoyan.items import MaoyanItem

class SpiderSpider(scrapy.Spider):
    # 定义爬虫名字
    name = 'spider'
    allowed_domains = ['maoyan.com']
    # 起始 url 列表
    start_urls = ['https://maoyan.com/board/4']

    # def parse(self, response):
    #     pass

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初识的请求对象（Request）。
    # start_requests() 方法读取 start_urls 列表中的 url 并生成 Requests 对象，发送给引擎
    # 引擎在指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        # for i in range(0,10):
        # 只取前十
        for i in range(0,1):
            url = f'https://maoyan.com/board/4?offset={i*10}'
            # url 请求访问的网址
            # callback 回调函数，引擎会将下载好的页面（Response 对象）发送给该方法，执行数据分析
            # 这里可以使用 callback 指定新的函数，不是用 parse 作为默认的回调参数
            yield scrapy.Request(url=url, callback=self.parse)

    # 解析函数
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'board-item-main'})
        for i in title_list:
            # 这里新增的 item 需要在 items.py 中相应增加
            item = MaoyanItem()
            title = i.find('a').get_text('title')
            link = 'https://maoyan.com'+i.find('a').get('href')
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        soup = BeautifulSoup(response.text, 'html.ppwdarser')
        movie_type = soup.find('li', attrs={'class': 'ellipsis'}).get_text().strip()
        item['movie_type'] = movie_type
        yield item