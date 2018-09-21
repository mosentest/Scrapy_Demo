# encoding=utf-8

import scrapy
import time


class WallpapersSpidersCls(scrapy.Spider):
    name = "WallpapersSpidersGo"
    start_urls = ['https://wallpapershome.com/']

    def parse(self, response):
        sel = scrapy.Selector(response)
        catalog_urls = sel.xpath('//div[@id="left-menu"]/ul/li/a/@href').extract()
        if catalog_urls:
            print("catalog_urls:" + str(catalog_urls))
        else:
            print("no urls")
        catalog_names = sel.xpath('//div[@id="left-menu"]/ul/li/a/text()').extract()
        if catalog_names:
            print("catalog_names:" + str(catalog_names))
        else:
            print("no names")
        for i in range(len(catalog_urls)):
            if i > 0:
                catalog_sub_url = "https://wallpapershome.com{0}".format(catalog_urls[i])
                print(catalog_sub_url)
                request = scrapy.http.Request(catalog_sub_url, callback=self.parse_page_item)
                # get url
                request.meta['url'] = catalog_sub_url;
                time.sleep(1)
                yield request

    def parse_page_item(self, response):
        baseUrl = response.meta['url']
        sel = scrapy.Selector(response)
        page_urls = sel.xpath('//p[@class="pages"]/a/@href').extract()
        # print("page_urls:" + str(page_urls))
        page_texts = sel.xpath('//p[@class="pages"]/a/text()').extract()
        # print("page_texts:" + str(page_texts))
        if 'Next' in page_texts:
            # print("page_urls[-1]:" + page_urls[-1])
            page_sub_url = baseUrl + "{0}".format(page_urls[-1])
            # print("page_sub_url:" + page_sub_url)
            request = scrapy.http.Request(page_sub_url, callback=self.parse_page_item)
            # set baseUrl
            request.meta['url'] = baseUrl;
            time.sleep(2)
            yield request
        links = sel.xpath('//div[@id="pics-list"]/p/a/@href').extract()
        if links:
            # print("读取当前页面的数据")
            # print(str(links))
            # 读取每个图片夹的连接
            for link in links:
                link_url = "https://wallpapershome.com{0}".format(link)
                request = scrapy.http.Request(link_url, callback=self.parse_item)
                time.sleep(1)
                yield request

    def parse_item(self, response):
        sel = scrapy.Selector(response)
        imgs = sel.xpath('//p[@id="main-pic"]/img[@class="hor"]/@src').extract()
        for img in imgs:
            print("url_here")
            img_url = "https://wallpapershome.com{0}".format(img)
            print("img_url:" + img_url)
        pass
