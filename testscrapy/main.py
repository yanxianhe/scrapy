# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/11/19 16:37:28
@Contact :   xianhe_yan@sina.com
'''
from scrapy import cmdline
from syslogs import GetLogging

GetLogging().get()
cmdline.execute('scrapy crawl scrapy'.split())