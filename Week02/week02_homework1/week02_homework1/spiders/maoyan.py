import scrapy,time
from bs4 import BeautifulSoup
from maoyan.items import MaoyanItem
from scrapy.selector import Selector

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    def start_requests(self):
        url = f'https://maoyan.com/board/4?offset=0'
        yield scrapy.Request(url=url, callback=self.parse)

    # 解析函数
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-item-info"]')
        try:
            for movie in movies:
                item = MaoyanItem()
                # extract 方法会将输出的 xpath 数据列表化，first 是取第一个
                title = movie.xpath('./p[@class="name"]/a/@title').extract_first().strip()
                link = 'https://maoyan.com'+movie.xpath('./p[@class="name"]/a/@href').extract_first().strip()
                item['title'] = title
                item['link'] = link
                yield scrapy.Request(url=link, meta={'item': item}, callback=self.parse2)
        except Exception as e:
            print(e)

    def parse2(self, response):
        item = response.meta['item']
        movie_type = Selector(response=response).xpath('//div[@class="movie-brief-container"]/ul/li[@class="ellipsis"]/a/text()').extract()
        item['movie_type'] = movie_type
        time.sleep(3)
        yield item