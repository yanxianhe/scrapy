#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request

from lxml import etree

Serialid = 'ca6f2d37da3b11eba16d0021cc64f539'
temp_sql='INSERT INTO `test`.`test_info` (`id`,  `storagetime`,  `numb`,  `start`,  `info`)   VALUES (%s,%s,%s,%s,%s)'
data=[('202107011513-ca6f2d36da3b11eba16d0021cc64f539', '2021-07-01 15:13:09', '1', '3885115', '就是因为没人看，我才敢发上来的')]


loginfo = ("{%s::}sql_insert  ------>" % (str(Serialid+temp_sql))) + "\r\n" + ("{%s::}sql_insert_data ------>" % (Serialid+str(data)))
href_link="http://www.beijing.gov.cn/ywdt/zyldhd/202107/t20210701_2426610.html"


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
req = urllib.request.Request(url=href_link, headers=headers)  

data=urllib.request.urlopen(req).read().decode('UTF-8') 

to_HTML_text = etree.HTML(data).xpath(".//div[@class='view TRS_UEDITOR trs_paper_default trs_web']//text()")
#    lists = response.xpath("//div[@class='tab_bd']//ul[@class='council_list2']/li")
to_HTML = str(to_HTML_text).replace("\\u3000", "&nbsp").replace("[","\"").replace("]","\"");
print( ":::::::::::: { %s  } ::::::::::::::" % str(to_HTML))