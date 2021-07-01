# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/11/20 10:45:01
@Contact :   xianhe_yan@sina.com
'''

import uuid
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
        # 标识号
        self.Serialid = str(uuid.uuid1()).replace("-", "")
        # 打开数据库连接
        self.db = pymysql.connect(host=host,port=port,user=username,password=password,db=dbname,charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    
    # mysql insert
    def insert_sql(self,temp_sql,data) :
        Serialid = self.Serialid
        loginfo = ("{%s::}sql_insert  ------>" % (str(Serialid+temp_sql))) + "\r\n" + ("{%s::}sql_insert_data ------>" % (Serialid+str(data)))
        logger.info(str(loginfo))
        try:
            # 使用cursor()方法获取操作游标 
            cur = self.db.cursor()
            cur.executemany(temp_sql,data)
            self.db.commit()
            return True
        except Exception as e :
            logger.error("SQL ERROR ------>" + str(Serialid + "::" + e))
            self.db.rollback()
            return False
        finally:
            # 关闭指针对象
            cur.close()
            # 关闭数据库连接对象
            self.db.close()

    # select fetchone
    def select_fetchone(self,temp_sql) :
        try:
            # 使用cursor()方法获取操作游标 
            cur = self.db.cursor()
            logger.info("sql_select ------>" + temp_sql)
            cur.execute(temp_sql)
            result = cur.fetchone()
            return (result)
        except Exception as e :
            logger.error("SQL ERROR ------>" + e)
            return e
        finally:
            # 关闭指针对象
            cur.close()
            # 关闭数据库连接对象
            self.db.close()

    # select list
    def select_list(self,temp_sql) :
        try:
            # 使用cursor()方法获取操作游标 
            cur = self.db.cursor()
            logger.info("sql_select ------>" + temp_sql)
            cur.execute(temp_sql)
            result = cur.fetchone()
            return (result)
        except Exception as e :
            logger.error("SQL ERROR ------>" + e)
            return e 
        finally:
            # 关闭指针对象
            cur.close()
            # 关闭数据库连接对象
            self.db.close()
