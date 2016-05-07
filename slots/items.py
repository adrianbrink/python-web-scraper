# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SlotsItem(scrapy.Item):
    # define the fields for your item here like:
    released = scrapy.Field()
    slot_type = scrapy.Field()
    house_edge = scrapy.Field()
    pass
