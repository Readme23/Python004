#!/usr/bin/env python
#encoding=utf-8
'''
安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、
电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中
'''
import pandas as pd
import requests,time,lxml.etree
from bs4 import BeautifulSoup as bs

# 构造用户请求头之 user-agent、cookie
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
cookie = '__mta=213741867.1600772885375.1601104618816.1601104684586.28; uuid_n_v=v1; uuid=E2F3EB40FCC311EA805853CB23A5B1A285BCF36FED4A4C44A50EF53CFC8C413B; _csrf=4fd1aa1a4c9e0a48ac047a897d465584434ff1d526fd89248e5352995e499bb9; mojo-uuid=7d22f6923017b3ae5f554017d6a1af63; _lxsdk_cuid=174b57fc9b5c8-08d9f61b26ac2d-31627402-13c680-174b57fc9b5c8; _lxsdk=E2F3EB40FCC311EA805853CB23A5B1A285BCF36FED4A4C44A50EF53CFC8C413B; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1600772885,1600772909; mojo-session-id={"id":"fd3ce923b3b357ad7019f693ca4c6a37","time":1601104401771}; __mta=213741867.1600772885375.1601104603072.1601104609506.29; mojo-trace-id=12; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601104684; _lxsdk_s=174c9425363-0f7-297-dbd%7C%7C23'
# 构造请求头
header = {
            'user-agent':user_agent,
            'Cookie':cookie
         }
# 目标网址
maoyan_url = 'http://maoyan.com/board/4'

def spider(url):
    # 请求返回
    response = requests.get(url,headers=header)
    # 获取返回码
    print(response.status_code)
    # 使用 bs 解析 html 网页
    bs_info = bs(response.text, 'html.parser')
    print(response.text)
    # 获取链接
    movie_href = []
    for tags in bs_info.find_all('div', attrs={'class': 'movie-item-info'}):
        for atag in tags.find_all('a',):
            time.sleep(1)
            # 获取链接
            movie_url = ('https://maoyan.com'+atag.get('href'))
            movie_href.append(movie_url)
    return movie_href

def full_data(full_url_list):
    for maoyan_href in full_url_list:
        # 请求返回
        response = requests.get(maoyan_href,headers=header)
        # xml 化处理
        selector = lxml.etree.HTML(response.text)
        # 电影名称
        movie_name = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/h1/text()')
        # 上映时间
        plan_date = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()')
        # 类型
        movie_type = selector.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()')
        # 全数据
        full_data = {}
        full_data[movie_name] = [movie_type,plan_date]
    return full_data

# 函数调用
movie_href = spider(maoyan_url)
full_data = full_data(movie_href)

# 写入本地文件
movie_maoyan = pd.DataFrame(data = full_data)
movie_maoyan.to_csv('./movie_douban.csv, encoding=utf-8, index=False, header=False')