# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class BotcnblogsItem(Item):
    # define the fields for your item here like:
    title = Field()             # 文章标题
    publishDate = Field()       # 发布日期
    readCount = Field()         # 阅读数
    commentCount = Field()      # 评论数
    pass
