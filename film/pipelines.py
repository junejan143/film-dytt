# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import FilmItem
import json
import codecs

# class FilmPipeline(object):
#     ## 爬虫的分析结果都会由scrapy交给此函数处理
#     def process_item(self, item, spider):
#         if isinstance(item, FilmItem):
#             ## 在此可进行文件写入、数据库写入等操作
#             pass
#         return item


class JsonWriterPipeline(object):
    def __init__(self):
        self.file = codecs.open('film.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode('unicode_escape'))
        return item