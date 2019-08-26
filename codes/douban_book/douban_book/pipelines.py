# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 这里是根据第二课的内容写的一个操作 Mongo 的类
from douban_book.helper.mongo_client import get_mongo


class DoubanBookPipeline(object):
    def process_item(self, item, spider):
        return item


class DoubanBookListPipeline(object):
    def __init__(self):
        # 获取 Mongo 客户端
        self.client = get_mongo('douban_book', 'book_list')

    def close_spider(self, spider):
        # 关闭 Mongo 客户端
        self.client.close()

    def process_item(self, item, spider):
        # 在接收到 Item 的时候，将他存储到 Mongo 中
        self.client.insert(dict(item))
        return item
