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
    primaryKey = scrapy.Field()
    # 默认值 2 
    top = scrapy.Field()
    # 赋值 34
    type = scrapy.Field()

    # 赋值 3401 
    classify = scrapy.Field()

    # 标题
    title = scrapy.Field()
    href = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 管理账户
    record_name = scrapy.Field()
    # 赋值 1
    record_id = scrapy.Field()
    # 入库时间
    record_date = scrapy.Field()
    # 赋值 1
    company_id = scrapy.Field()
    price = scrapy.Field()
    order_number = scrapy.Field()
    is_have_preview = scrapy.Field()
    preview = scrapy.Field()
    browse_number = scrapy.Field()
    publisher = scrapy.Field()
    # 发布日期
    recomend_time = scrapy.Field()
 
