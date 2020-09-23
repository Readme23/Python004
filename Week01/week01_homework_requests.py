#!/usr/bin/env python
#encoding=utf-8
'''
安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、
电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中
'''
import requests
from bs4 import BeautifulSoup as bs

# 构造用户请求头之 user-agent、cookie
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
cookie = '__mta=213741867.1600772885375.1600839489915.1600843159369.20; uuid_n_v=v1; uuid=E2F3EB40FCC311EA805853CB23A5B1A285BCF36FED4A4C44A50EF53CFC8C413B; _csrf=4fd1aa1a4c9e0a48ac047a897d465584434ff1d526fd89248e5352995e499bb9; mojo-uuid=7d22f6923017b3ae5f554017d6a1af63; _lxsdk_cuid=174b57fc9b5c8-08d9f61b26ac2d-31627402-13c680-174b57fc9b5c8; _lxsdk=E2F3EB40FCC311EA805853CB23A5B1A285BCF36FED4A4C44A50EF53CFC8C413B; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1600772885,1600772909; mojo-session-id={"id":"81734707c7bbcc843daf9395cc09dfd9","time":1600839248686}; __mta=213741867.1600772885375.1600839489915.1600841133620.20; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1600843159; mojo-trace-id=30; _lxsdk_s=174b9aff48b-867-9e0-d9e%7C%7C5'
# 构造请求头
header = {
            'user-agent':user_agent,
            'Cookie':cookie
         }
# 目标网址
my_url = 'https://maoyan.com/board/4'
# 请求返回
response = requests.get(my_url,headers=header)
# 使用 bs 解析 html 网页
bs_info = bs(response.text, 'html.parser')
# http 返回码
print(f'返回码是：{response.status_code}')

for tags in bs_info.find_all('div', attrs={'class': 'movie-item-info'}):
    for atag in tags.find_all('a',):
        # 获取电影名称
        print(atag.get('title',))
        # 获取电影链接
        print('https://maoyan.com'+atag.get('href'))
# print(response.text)
