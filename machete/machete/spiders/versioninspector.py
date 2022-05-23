import scrapy
import re
from scrapy.loader import ItemLoader
from machete.items import VersionItem

class versionSpider(scrapy.Spider):
    name = 'versioninspector'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'FEED_URI': 'acordeones.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    start_urls = ['https://reactjs.org']

    def parse(self, response):
        i = 0
        item = ItemLoader(item=VersionItem(), response=response)
        item.add_xpath('version', '//header//div/a[@href="/versions"]/text()[2]')
        item._add_value('source', self.start_urls[i])  
        i = i+1
        yield item.load_item()

        #   //header//div/a[@href="/versions"]/text()[2]                             react

        #  //h1/text()           scrapy

        # REGEX DE VERSION    \d+\.\d+\.*\d*

        # REGEX MEJOR           \d{1,2}\.\d{1,2}\.?\d{0,2}

        #                     [\d]{1,2}\.[\d]{1,2}\.{0,1}\d{0,2}