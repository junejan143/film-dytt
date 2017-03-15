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

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

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

        next_page = selector.xpath("//div[@class='co_content8']/div//a[7]/@href").extract_first()
        if  next_page:
            print next_page
            next_page = "http://www.ygdy8.net/html/gndy/dyzz/" + next_page
            print next_page
            self.log('page_url: %s' % next_page)
            ## 将 「下一页」的链接传递给自身，并重新分析
            yield Request(next_page, callback=self.parse)

    def parse_topic(self, response):
        selector = Selector(response)
        url = selector.xpath("//*[@id='Zoom']//table//a/text()").extract_first()
        print url
        return url
        # 可以在此处解析翻页信息，从而实现爬取帖子的多个页面
