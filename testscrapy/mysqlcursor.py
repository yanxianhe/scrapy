# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/11/20 10:45:01
@Contact :   xianhe_yan@sina.com
'''
import pymysql
from loguru import logger
from testscrapy.settings import *


class mysqlcursor (object) :
    def __init__(self) :
        host = mysql_host
        port = mysql_port
        username = mysql_db_user
        password = mysql_db_pwd
        dbname = mysql_db_name 
        self.cursor = pymysql.connect(host=host,port=port,user=username,password=password,db=dbname,charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    def insert_sql(self,temp,data) :
        cur = self.cursor.cursor()
        try:
            logger.info("SQL_TEMP ------>" + temp)
            logger.info("SQL_DATA ------>" + str(data))
            cur.executemany(temp,data)
            self.cursor.commit()
            return True
        except Exception as e :
            logger.error("SQL ------>" + e)
            self.cursor.rollback()
            return False
        finally:
            cur.close()
