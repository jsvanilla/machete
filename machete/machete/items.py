# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MacheteItem(scrapy.Item):
    question = scrapy.Field()
    answer = scrapy.Field()
    example = scrapy.Field()
    topic = scrapy.Field()
    tags = scrapy.Field()
    multiprocessId = scrapy.Field() 
    version = scrapy.Field()
    
class VersionItem(scrapy.Item):
    version = scrapy.Field()
    source = scrapy.Field()