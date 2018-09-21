#!/usr/bin/env python
# encoding=utf-8

import scrapy
import time
from aaa.items import AaaItem


class DemoSpider(scrapy.Spider):
    name = "aaa"
    start_urls = [
        "http://meizitu.com/a/more_1.html"
    ]

    def parse(self, response):
        selector = scrapy.Selector(response);
        next_pages = selector.xpath('//*[@id="wp_page_numbers"]/ul/li/a/@href').extract()
        print("我是页面的超链接")
        print(next_pages)
        print("我是页面的内容")
        next_pages_text = selector.xpath('//*[@id="wp_page_numbers"]/ul/li/a/text()').extract()
        print(next_pages_text)
        if '下一页' in next_pages_text:
            print("当前页面：" + next_pages[-2])
            next_url = "http://www.meizitu.com/a/{0}".format(next_pages[-2])
            with open('url.txt', 'a+') as fp:
                fp.write('\n')
                fp.write(next_url)
                fp.write("\n")
            request = scrapy.http.Request(next_url, callback=self.parse)
            time.sleep(2)
            yield request

        links = selector.xpath('//div[@class="pic"]/a/@href').extract()
        print("开始打印文件夹")
        print(links)
        # 读取每个图片夹的连接
        for link in links:
            request = scrapy.http.Request(link, callback=self.parse_item)
            time.sleep(1)
            yield request

    def parse_item(self, response):
        aaaItem = AaaItem()
        selector = scrapy.Selector(response);
        img = selector.xpath('//*[@id="picture"]/p/img/@src').extract()
        print("开始打印图片")
        print(img)
        time.sleep(1)
        aaaItem['src'] = img
        yield aaaItem
