# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline:
    # def process_item(self, item, spider):
    #     return item
    # 每一个 item 管道组件都会调用该方法，并且必须返回一个 item 对象实例或 raise DropItem 异常
    def process_item(self, item, spider):
        title = item['title']
        link = item['link']
        movie_type = item['movie_type']
        output = f'|{title}|\t|{link}|\t|{movie_type}|\n\n'
        with open('./maoyan.txt', 'a+', encoding='utf-8') as movie_file:
            movie_file.write(output)
        return item