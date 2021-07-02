# -*- coding: utf-8 -*-

from testscrapy.mysqlcursor import mysqlcursor


from testscrapy.settings import mysql_host,mysql_port,mysql_db_name,mysql_db_collection,mysql_db_user,mysql_db_pwd


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class TestscrapyPipeline:
    #def __init__(self) :
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
        lists = (data["top"],data["type"],data["classify"],data["title"],data["content"],data["record_name"],data["record_id"],data["record_date"],data["company_id"],data["price"],data["order_number"],data["is_have_preview"],data["preview"],data["browse_number"],data["publisher"])
        valuesList.append(lists)
        temp = "INSERT INTO `test`.`src_h5_model` (`top`,`type`,`classify`,`title`,`content`,`record_name`,`record_id`,`record_date`,`company_id`,`price`,`order_number`,`is_have_preview`,`preview`,`browse_number`,`publisher`)   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_conn = mysqlcursor().insert_sql(temp, valuesList)
        return sql_conn
