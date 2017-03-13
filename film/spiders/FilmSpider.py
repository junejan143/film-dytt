# coding=utf-8
import scrapy
from scrapy import Selector

class FilmSpider(scrapy.Spider):
    name = "film"
    host = "http://www.ygdy8.net"
    start_urls = [
        "http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html"
    ]

    def parse(self, response):
        selector = Selector(response)
        #    //table[@class='tbspan']
        content_list = selector.xpath("//a[@class='ulink'] ")
        # 遍历这个list，处理每一个标签
        for content in content_list:
            # 此处解析标签，提取出我们需要的帖子标题。
            topic = content.xpath('string(.)').extract_first()
            print topic
            # 此处提取出帖子的url地址。
            url = self.host + content.xpath('@href').extract_first()
            print url