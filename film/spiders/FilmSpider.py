# coding=utf-8
import scrapy
from scrapy import Selector
from scrapy import Request
from ..items import FilmItem

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
            item = FilmItem()
            title = content.xpath('string(.)').extract_first()
            item["title"] = title
            # 此处提取出帖子的url地址。
            url = self.host + content.xpath('@href').extract_first()
            print url
            yield Request(url=url, callback=self.parse_topic)

    def parse_topic(self, response):
        selector = Selector(response)
        url = selector.xpath("//*[@id='Zoom']//table//a")
        url = url.xpath('string(.)').extract_first()
        # item["url"] = url
        print url
        # 可以在此处解析翻页信息，从而实现爬取帖子的多个页面

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield Request(url=url, callback=self.parse_page)