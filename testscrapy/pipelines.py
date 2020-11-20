# -*- coding: utf-8 -*-

import pymongo
from loguru import logger
from testscrapy.mysqlcursor import mysqlcursor
from testscrapy.syslogs import GetLogging

from testscrapy.settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection,mongo_db_user,mongo_db_pwd


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class TestscrapyPipeline:
    def __init__(self) :
        GetLogging().get()
        #host = mongo_host
        #port = mongo_port
        #username = mongo_db_user
        #password = mongo_db_pwd
        #dbname = mongo_db_name
        #sheetname = mongo_db_collection
        #client = pymongo.MongoClient(host=host,port=port,username=username, password=password,authMechanism='SCRAM-SHA-256')
        #mydb = client[dbname]
        #self.post = mydb[sheetname]

    def process_item(self, item, spider):
        data = dict(item)
        #self.post.insert(data)
        valuesList = []
        lists = (data["id"],data["storagetime"],data["numb"],data["star"],data["info"])
        valuesList.append(lists)
        temp = "INSERT INTO `test`.`test_info` (`id`,  `storagetime`,  `numb`,  `start`,  `info`)   VALUES (%s,%s,%s,%s,%s)"
        sql_conn = mysqlcursor().insert_sql(temp, valuesList)
        return sql_conn
