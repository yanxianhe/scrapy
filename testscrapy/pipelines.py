# -*- coding: utf-8 -*-

import pymongo

from testscrapy.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection,mongo_db_user,mongo_db_pwd
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class TestscrapyPipeline:
    def __init__(self):
        host = mongo_host
        port = mongo_port
        username = mongo_db_user
        password = mongo_db_pwd
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        client = pymongo.MongoClient(host=host,port=port,username=username, password=password,authMechanism='SCRAM-SHA-256')
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
