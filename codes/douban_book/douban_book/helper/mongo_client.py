# 导入连接 MongoDB 的包
from pymongo import MongoClient

__mongo_client = {}


def get_mongo_client(db='douban_book', table='unknown'):
    if f'{db}-{table}' in __mongo_client:
        return __mongo_client[f'{db}-{table}']

    # 创建连接
    client = MongoClient('mongodb://localhost:27017/')

    # 指定数据库
    db = getattr(client, db)

    # 指定数据库中的一个表
    client = getattr(db, table)
    __mongo_client[f'{db}-{table}'] = client
    return client


class Mongo(object):
    def __init__(self, db, table):
        self.client = get_mongo_client(db, table)

    def insert(self, data):
        return self.client.insert_one(data)

    def update(self, filter, update):
        return self.client.update(filter, update)

    def delete(self, filter):
        return self.client.remove(filter)

    def close(self):
        return self.client.close()


def get_mongo(db, table):
    return Mongo(db, table)
