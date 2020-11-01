# -*- coding: utf-8 -*-
import scrapy,time
from douban_movie.items import DoubanMovieItem
from scrapy.selector import Selector

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']
    
    def start_requests(self):
        # for i in range(0, 10):
        i = 0
        url = f'https://movie.douban.com/top250?start={i*25}'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="hd"]')
        for movie in movies:
            item = DoubanMovieItem()
            title = movie.xpath('./a/span[1]/text()').extract()
            link = str(movie.xpath('./a/@href').extract()[0])+'comments?status=P'
            item['title'] = title
            item['link'] = link
            yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)

    def parse2(self, response):
        item = response.meta['item']
        evaluate = Selector(response=response).xpath('//span[@class="short"]/text()').extract()
        for short_evaluate in evaluate:
            item['short_evaluate'] = short_evaluate
            star = Selector(response=response).xpath('//span[@class="comment-info"]/span/@title').extract_first()
            item['star'] = star
        # short_evaluate = ''.join(short_evaluate)
            yield item