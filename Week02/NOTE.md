## 一 、异常捕获与处理
1. pretty_errors 官方文档链接：
https://pypi.org/project/pretty-errors/
2. try 语句官方文档：
https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-try-statement
3. with 语句官方文档：
https://docs.python.org/zh-cn/3.7/reference/compound_stmts.html#the-with-statement
4. with 语句上下文管理器官方文档：
https://docs.python.org/zh-cn/3.7/reference/datamodel.html#with-statement-context-managers
### 异常处理机制的原理
  - 异常也是一个类
  - 异常捕获的过程：
    - 异常类把错误消息打包到一个对象
    - 然后该对象会自动查找到调用栈
    - 知道运行系统找到明确声明如何处理这些类异常的位置
  - 所有异常都继承自 BaseException
  - Traceback 显示了出错的位置，显示的顺序和异常信息对象传播的方向是相反的
### 异常信息与异常捕获
  - 异常信息在 Traceback 信息的最后一行，有不同的类型
  - 捕获异常可以使用 try...except 语法
  - try...except 支持多重异常处理
#### 常见的异常类型
  1. LookupError 下的 IndexError 和 KeyError
  2. IOError
  3. NameError
  4. TypeError
  5. AttributeError
  6. ZeroDivisionError
### 自定义异常
```
# 继承父类 Exception
class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo

userinput = 'a'

try:
    if (not userinput.isdigit()):
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
# 无论异常是否发生，finally 语句都会被执行
finally:
    del userinput
```
### 美化异常输出
  - 安装：pip3 install pretty_errors
  - 使用：import pretty_errors
## 二、使用 PyMySQL 进行数据库操作
1. MySQL 官方文档手册：https://dev.mysql.com/doc/
2. MySQL 官方下载连接：https://dev.mysql.com/downloads/mysql/
3. PyMySQL 官方文档: https://pypi.org/project/PyMySQL/
### 安装
  - pip3 install pymsql
### 链接
  - 开始 -- 创建 connection -- 获取 cursor-CRUD（查询并获取数据）-- 关闭 cursor -- 关闭 connection -- 结束
```
import pymsql

dbInfo = {
    'host': 'localhost',
    'prot': '3306',
    'user': 'root',
    'password': 'admin',
    'db': 'pythontrain'
    'charset': 'utf8mb4'
}

sqls = ['select 1', 'select VERSION()']

result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self,host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.charset = dbInfo['charset']
        self.sqls = sqls

    def run(self):
        conn = pymsql.connect(
            host = self.host,
            prot = self.port,
            user = self.user,
            password = self.password,
            charset = self.charset,
            db = self,db
        )
        # 游标建立的时候就开启了一个隐形的事务
        cur = conn.cursor()
        try:
            for command in self.sqls:
                cur.execute(command)
                # cur.fetchone() 返回结果的第一条，cur.fetchall()
                result.append(cur.fetchone())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            # 出现异常就回退
            conn.rollback()
        # 关闭数据库链接
        conn.close()

# 执行
if __name__ == 'main':
    db = ConnDB(dbInfo, sqls)
    db.run()
    print(result)

# 执行批量插入
values = [(id,'teachers'+str(id)) for id in range(4, 21)]
cursor.executemany('INSERT INTO' + TABLE_NAME + 'values(%s,%s)', values)
```
## 三、反爬虫：模拟浏览器的头部信息
1. User-Agent 参考文档：https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/User-Agent
### 浏览器基本行为
1. 带 http 头信息：如 User-Agent、Referer 等
2. 带 cookies（包含加密的用户名、密码验证信息）
### 设置随机 User-Agent
```
# pip3 install fake-useragent
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)

# 模拟不同的浏览器
print(f'Chrome 浏览器': {ua.chrome})
print(ua.safari)
print(ua.ie)

# 随机返回头部信息，推荐使用
print(f'随机浏览器：{ua.random}')
```
## 四、反爬虫：cookies 验证
1、httpbin 网址：https://httpbin.org/
### http 协议的 get 方法
```
import requests
r = requests.get('https://github.com')
r.status_code
r.headers['content-type']
# r.text
r.encoding
# r.json()
```
### http 协议的 post 方法
```
import requests
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r.json()
```
### 保存 cookies
```
import requests
# 在同一个 Session 实例发出的所有请求之间保持 cookie
s = requests.Session()

s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")

print(r.text)
#'{"cookies": {"sessioncookie": "123456789"}}'

# 会话可以使用上下文管理器
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
```
#### cookies requests
```
import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
# 随机的 User-Agent
'User-Agent' : ua.random,
'Referer' : 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
s = requests.Session()
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
# 这些数据需要到浏览器的“检查”里面去找
form_data = {
'ck':'',
'name':'15055495@qq.com',
'password':'',
'remember':'false',
'ticket':''
}

# post数据前获取cookie
pre_login = 'https://accounts.douban.com/passport/login'
pre_resp = s.get(pre_login, headers=headers)

response = s.post(login_url, data=form_data, headers=headers, cookies=s.cookies)

# 登陆后可以进行后续的请求
# url2 = 'https://accounts.douban.com/passport/setting'

# response2 = s.get(url2,headers = headers)
# response3 = newsession.get(url3, headers = headers, cookies = s.cookies)

# with open('profile.html','w+') as f:
    # f.write(response2.text)
```
## 五、反爬虫：使用 WebDriver 模拟浏览器行为
1. WebDriver 文档：https://www.w3.org/TR/webdriver/，https://www.selenium.dev/selenium/docs/api/py/
2. ChromeDriver 下载地址：https://chromedriver.storage.googleapis.com/index.html
### 安装
  - pip3 install selenium
  - 代码实现
```
from selenium import webdriver
import time

try:
    # 需要安装chrome driver, 和浏览器版本保持一致
    # http://chromedriver.storage.googleapis.com/index.html
    browser = webdriver.Chrome()
    
    browser.get('https://www.douban.com')
    time.sleep(1)

    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    btm1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    btm1.click()

    browser.find_element_by_xpath('//*[@id="username"]').send_keys('15055495@qq.com')
    browser.find_element_by_id('password').send_keys('test123test456')
    time.sleep(1)
    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()

    # 获取cookies
    cookies = browser.get_cookies() 
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)
finally:    
    browser.close()
```
### eg
```
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
   
    browser.get('https://movie.douban.com/subject/1292052/')
    time.sleep(1)


    btm1 = browser.find_element_by_xpath('//*[@id="hot-comments"]/a')
    btm1.click()
    time.sleep(10)
    print(browser.page_source)

except Exception as e:
    print(e)
# finally:    
#     browser.close()
```
#### 分快下载
```
########## 小文件下载：
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
r = requests.get(image_url)
with open("python_logo.png",'wb') as f:
    f.write(r.content)

############# 大文件下载：
# 如果文件比较大的话，那么下载下来的文件先放在内存中，内存还是比较有压力的。
# 所以为了防止内存不够用的现象出现，我们要想办法把下载的文件分块写到磁盘中。
import requests
file_url = "http://python.xxx.yyy.pdf"
# stream=True 表示流式下载
r = requests.get(file_url, stream=True)
with open("python.pdf", "wb") as pdf:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            pdf.write(chunk)
```
## 六、反爬虫：验证码识别
1. 各种语言识别库：https://github.com/tesseract-ocr/tessdata
### 安装使用
```
# 先安装依赖库libpng, jpeg, libtiff, leptonica
# brew install leptonica
# 安装tesseract
# brew install  tesseract
# 与python对接需要安装的包
# pip3 install Pillow
# pip3 install pytesseract



import requests
import os
from PIL import Image
import pytesseract

# 下载图片
# session = requests.session()
# img_url = 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1320441599,4127074888&fm=26&gp=0.jpg'
# agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# headers = {'User-Agent': agent}
# r = session.get(img_url, headers=headers)

# with open('cap.jpg', 'wb') as f:
#     f.write(r.content)

# 打开并显示文件
im = Image.open('cap.jpg')
im.show()

# 灰度图片
gray = im.convert('L')
gray.save('c_gray2.jpg')
im.close()

# 二值化
threshold = 100
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

out = gray.point(table, '1')
out.save('c_th.jpg')

th = Image.open('c_th.jpg')
print(pytesseract.image_to_string(th,lang='chi_sim+eng'))

# 各种语言识别库 https://github.com/tesseract-ocr/tessdata
# 放到 /usr/local/Cellar/tesseract/版本/share/tessdata
```
## 七、爬虫中间件&系统代理 IP
  ### 示例代码
```
import scrapy

# export http_proxy='http://52.179.231.206:80'
# setting 增加 scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware
# 通过 Request.meta['proxy'] 读取 http_proxy 环境变量加载代理


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    # 通过ip查看请求的ip地址
    start_urls = ['http://httpbin.org/ip']
    # 通过header 查看user-agent
    # start_urls = ['http://httpbin.org/headers']

    def parse(self, response):
        print(response.text)

```
1. scrapy crawl spider_name --nolog # 不打印日志
2. settings.py 中以下代码默认是注释的，需要打开注释，后边的数字表示优先级，数字越小，优先级越低
```
DOWNLOADER_MIDDLEWARES = {
    'proxyspider.middlewares.ProxyspiderDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 400,
}
```
## 八、自定义中间件&随机代理 ip
### 如何编写一个下载中间件
1. process_request(request, spider) # Request 对象经过下载中间件时会被调用，优先级高的先调用
2. process_response(request, response, spider) # Response 对象经过下载中间件时会被调用，优先级高的后调用
3. process_exception(request, exception, spider) # 当 process_exception() 和 process_request() 抛出异常时会被调用
4. from_crawler(cls, crawler) # 使用 crawler 来创建中间件对象，并（必须）返回中间件对象
5. 示例代码
```
# settings.py 修改
DOWNLOADER_MIDDLEWARES = {
    'proxyspider.middlewares.ProxyspiderDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'proxyspider.middlewares.RandomHttpProxyMiddleware': 400,

}
HTTP_PROXY_LIST = [
     'http://52.179.231.206:80',
     'http://95.0.194.241:9090',
]

vim middlewares.py
# 因为要继承类，所以先引入原有的类
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.exceptions import NotConfigured
from urllib.parse import urlparse

class RandomHttpProxyMiddleware(HttpProxyMiddleware):

    def __init__(self, auth_encoding='utf-8', proxy_list = None):
        self.proxies = defaultdict(list)
        for proxy in proxy_list:
            parse = urlparse(proxy)
            self.proxies[parse.scheme].append(proxy)

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.get('HTTP_PROXY_LIST'):
            raise NotConfigured

        http_proxy_list = crawler.settings.get('HTTP_PROXY_LIST')  
        auth_encoding = crawler.settings.get('HTTPPROXY_AUTH_ENCODING', 'utf-8')

        return cls(auth_encoding, http_proxy_list)

    def _set_proxy(self, request, scheme):
        proxy = random.choice(self.proxies[scheme])
        request.meta['proxy'] = proxy

class ProxyspiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
```
## 九、分布式爬虫
### 实现
#### scrapy 原生不支持分布式，多机之间需要 redis 实现队列和管道的共享，scrapy-redis 很好的实现了 scrapy 和 redis 的集成
1. 使用了 redisspider 类替代了 spider 类
2. scheduler 的 queue 由 redis 实现
3. item pipeline 由 redis 实现
```
# 安装
pip3 install scrapy-redis

vim settings.py
# redis信息
REDIS_HOST='127.0.0.1'
REDIS_PORT=6379

# Scheduler的QUEUE
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Requests的默认优先级队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'

# 将Requests队列持久化到Redis，可支持暂停或重启爬虫
SCHEDULER_PERSIST = True

# 将爬取到的items保存到Redis
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}
```