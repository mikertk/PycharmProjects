#!/usr/bin/env
# coding:utf-8
"""
Author = miker
Created on 2017/3/14 14:24
Description:

"""
import sys
from firstSpiders.items import FirstspidersItem
import scrapy

reload(sys)
sys.setdefaultencoding('utf-8')


class testSpider(scrapy.spiders.Spider):
    name = "testFirst"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.xpath('//ul/li'):
            # title = sel.xpath('a/text()').extract()
            # link = sel.xpath('a/@href').extract()
            # desc = sel.xpath('text()').extract()
            # # print ('title:%-10s ', title, 'link:%-10s ', link, 'desc:%-10s ', desc)
            # print ('title:%-50s link:%-50s desc:%-50s' % (title, link, desc))
            item = FirstspidersItem()
            item['title'] = sel.xpath("a/text()").extract()
            yield item
