# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AaaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #title文件夹名字
    title=scrapy.Field()
    url=scrapy.Field()
    tags=scrapy.Field()
    #图片连接
    src=scrapy.Field()
    #alt图片名字
    alt=scrapy.Field()
    pass
