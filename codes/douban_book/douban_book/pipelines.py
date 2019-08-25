# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from douban_book.helper.mongo_client import get_mongo


class DoubanBookPipeline(object):
    def process_item(self, item, spider):
        return item


class DoubanBookListPipeline(object):
    def __init__(self):
        self.client = get_mongo('douban_book', 'book_list')

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.client.insert(dict(item))
        return item
