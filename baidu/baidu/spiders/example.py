# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        # print(response.body.decode())
        title = response.xpath('//title/text()').extract()
        search_button_text = response.xpath('//input[@class="bg s_btn"]/@value').extract()
        print(title)
        print(search_button_text)

        title = response.xpath('//title/text()')
        title_1 = title.extract()[0]
        title_2 = title[0].extract()
