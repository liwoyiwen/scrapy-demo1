# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class JianshuPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient(host='192.168.100.166', port=27017)
        db = client['scrapy']
        jianshu = db["data"]
        self.post = jianshu

    def process_item(self, item, spider):
        info = dict(item)
        self.post.insert(info)
        return item
