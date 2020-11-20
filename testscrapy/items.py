# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/11/19 16:37:59
@Contact :   xianhe_yan@sina.com
'''

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TestscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 序号
    id = scrapy.Field()
    # 入库日期
    storagetime = scrapy.Field()
    # 点击量
    numb = scrapy.Field()
    # 名称
    name = scrapy.Field()
    # 介绍
    info = scrapy.Field()
    # 星级
    star = scrapy.Field()
    # 评论
    ev = scrapy.Field()
    # 描述
    describe = scrapy.Field()
 
