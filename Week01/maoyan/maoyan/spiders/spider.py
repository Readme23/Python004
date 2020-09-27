# -*- coding: utf-8 -*-
import scrapy,time
from bs4 import BeautifulSoup
from maoyan.items import MaoyanItem
from scrapy.selector import Selector

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
        url = f'https://maoyan.com/board/4?offset=0'
        yield scrapy.Request(url=url, callback=self.parse)
            # url = f'https://maoyan.com/board/4?offset={i*10}'
            # url 请求访问的网址
            # callback 回调函数，引擎会将下载好的页面（Response 对象）发送给该方法，执行数据分析
            # 这里可以使用 callback 指定新的函数，不是用 parse 作为默认的回调参数
            # yield scrapy.Request(url=url, callback=self.parse)

    # 解析函数
    def parse(self, response):
        # bs4 写法
        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_list = soup.find_all('div', attrs={'class': 'board-item-main'})
        # for i in title_list:
        #     # 这里新增的 item 需要在 items.py 中相应增加
        #     item = MaoyanItem()
        #     title = i.find('a').get_text('title')
        #     link = 'https://maoyan.com'+i.find('a').get('href')
        #     item['title'] = title
        #     item['link'] = link
        #     yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
        # xpath 写法
        movies = Selector(response=response).xpath('//div[@class="movie-item-info"]')
        for movie in movies:
            item = MaoyanItem()
            # extract 方法会将输出的 xpath 数据列表化，first 是取第一个
            title = movie.xpath('./p[@class="name"]/a/@title').extract_first().strip()
            link = 'https://maoyan.com'+movie.xpath('./p[@class="name"]/a/@href').extract_first().strip()
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        # bs4 写法
        # soup = BeautifulSoup(response.text, 'html.parser')
        # movie_type = soup.find('li', attrs={'class': 'ellipsis'}).get_text().strip()
        # xpath 写法
        movie_type = Selector(response=response).xpath('//div[@class="movie-brief-container"]/ul/li[@class="ellipsis"]/a/text()').extract()
        item['movie_type'] = movie_type
        time.sleep(3)
        yield item