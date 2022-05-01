# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobparserItem(scrapy.Item):
    name = scrapy.Field()
    salary = scrapy.Field()
    link = scrapy.Field()
    min = scrapy.Field()
    max = scrapy.Field()
    curren = scrapy.Field()
    _id = scrapy.Field()

    pass
