学习笔记
# 用 requests 写一个简单的爬虫
## print 
  - python的print字符串前面加f表示格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式，如果字符串里面没有表达式，那么前面加不加f输出应该都一样
## requests 模块
  - request.get #模范浏览器访问 web 网站
  - eg.
    ```
    Requests is an HTTP library, written in Python, for human beings.
    Basic GET usage:

    >>> import requests
    >>> r = requests.get('https://www.python.org')
    >>> r.status_code
    200
    >>> b'Python is a programming language' in r.content
    True
    ```
## 获取 response 的内容
  - response.text

# 使用 beautifulsoup 解析爬取到的网页
## bs4 官网：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
  - 解析网页
    ```
    bs_info = bs(response.text, 'html.parser')
    ```
## 利用浏览器“查找”功能找到对应内容的标签
  - eg.
  ```
  for tags in bs_info.find_all('div', attrs={'class': 'movie-item-info'}):
    for atag in tags.find_all('a',):
        # 获取电影名称
        print(atag.get('title',))
        # 获取电影链接
        print('https://maoyan.com'+atag.get('href'))
    ```