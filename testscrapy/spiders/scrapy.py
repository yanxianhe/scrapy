# -*- coding: utf-8 -*-
'''
Created on 2020年6月8日

@author: yanxianhe
'''
import scrapy
from builtins import list
from testscrapy.items import TestscrapyItem
class DmozSpider(scrapy.Spider): # 继承Spider类
    name = "scrapy" # 爬虫的唯一标识，不能重复，启动爬虫的时候要用
    allowed_domains = ["bilibili.com"] # 限定域名，只爬取该域名下的网页
    start_url = "https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3"
    start_urls = [ # 开始爬取的链接
        start_url
    ]
    ## 默认解析
    def parse(self, response):
        # print(response.text)
        list = response.xpath("//div[@class='rank-list-wrap']//ul[@class='rank-list']/li")
        for i in list:
            ## 导入 Item
            test_Item = TestscrapyItem()
            ## 数据解析
            test_Item['numb'] = i.xpath(".//div[@class='num']//text()").extract_first()
            test_Item['star'] = i.xpath(".//div[@class='pts']//text()").extract_first()
            test_Item['info'] = i.xpath(".//div[@class='info']//text()").extract_first()
            ## 将数据yield to pipelines
            yield test_Item
        ## 下一页截取
        next_link = response.xpath("//span[@class='next']/link//@href").extract()
        if next_link:
            next_link = next_link[0]
            ## 回调
            yield scrapy.Request(start_url+next_link,callback=self.parse)

            
