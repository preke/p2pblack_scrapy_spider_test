# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ListItem(scrapy.Item):
    name = scrapy.Field()
    id_number = scrapy.Field()
    money = scrapy.Field()
    benjin = scrapy.Field()
    state = scrapy.Field()
    stage = scrapy.Field()
    _id = scrapy.Field()