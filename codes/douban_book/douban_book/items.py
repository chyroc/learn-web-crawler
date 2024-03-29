# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    img = scrapy.Field()
    href = scrapy.Field()
    title = scrapy.Field()
    about = scrapy.Field()
    rate = scrapy.Field()
    rate_count = scrapy.Field()
    desc = scrapy.Field()
