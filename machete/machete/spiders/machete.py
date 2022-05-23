from ensurepip import version
import scrapy
from scrapy.loader import ItemLoader
from machete.items import MacheteItem

class macheteSpider(scrapy.Spider):
    name = 'machete'
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'FEED_URI': 'acordeones.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    start_urls = ['https://reactjs.org']

    def parse(self, response):
        item = ItemLoader(item=MacheteItem(), response=response)
        item.add_xpath('version', '//*[@id="gatsby-focus-wrapper"]/div/header/div[2]/div/div/a[1]/text()[2]')
        yield item.load_item()