# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/11/19 16:38:13
@Contact :   xianhe_yan@sina.com
'''


import uuid
import datetime
import scrapy
import time
import urllib.request
from lxml import etree

from builtins import list
from testscrapy.items import TestscrapyItem
from loguru import logger

class DmozSpider(scrapy.Spider): # 继承Spider类
    name = "scrapy" # 爬虫的唯一标识，不能重复，启动爬虫的时候要用
    allowed_domains = ["beijing.gov.cn"] # 限定域名，只爬取该域名下的网页
    start_url = "http://www.beijing.gov.cn/"
    start_urls = [ # 开始爬取的链接
        start_url
    ]
    ## 默认解析
    def parse(self, response):
        # print(response.text)
        logger.debug(response.xpath)
        lists = response.xpath("//div[@class='tab_bd']//ul[@class='council_list2']/li")
        for i in lists :
            ## 导入 Item
            test_Item = TestscrapyItem()
            ## 数据解析
            minutes = datetime.datetime.now().strftime('%Y%m%d%H%M')
            ob_id =  str(minutes) + "-" + str(uuid.uuid1()).replace("-","")
            test_Item['top'] = 2
            test_Item['type'] = 34
            test_Item['classify'] = 3401
            title = i.xpath(".//span[@class='recomend_title']//a")
            href_link = title[0].attrib.get('href')
            title = title[0].attrib.get('title')
            test_Item['title'] = title
            test_Item['href']=href_link
            to_HTML_text = ""
            if href_link :
                headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
                req = urllib.request.Request(url=href_link, headers=headers)  
                data=urllib.request.urlopen(req).read().decode('UTF-8') 
                to_HTML_text = etree.HTML(data).xpath(".//div[@class='view TRS_UEDITOR trs_paper_default trs_web']//text()")
            #test_Item['content']  = str(to_HTML_text).replace("\\u3000", "&nbsp") ;
            test_Item['content']  = str(data) ;
            test_Item['record_name'] = "管理账户"
            test_Item['record_id'] = 1
            test_Item['record_date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            test_Item['company_id'] = 1
            test_Item['price'] = 1
            test_Item['order_number'] = ob_id
            test_Item['is_have_preview'] = 1
            test_Item['preview'] = ob_id[3:7]
            test_Item['browse_number'] =  ob_id[7:9]
            test_Item['publisher'] = 'gov'
            test_Item['recomend_time']=i.xpath(".//span[@class='recomend_time']//text()").extract_first()
            
            
            
            ## 将数据yield to pipelines
            logger.debug(test_Item)

            
            yield test_Item
        ## 下一页截取
        next_link = response.xpath("//span[@class='next']/link//@href").extract()
        if next_link:
            next_link = next_link[0]
            ## 回调
            yield scrapy.Request(start_url+next_link,callback=self.parse)