# -*- coding: utf-8 -*-
from dbmanager import MysqlCommond

mysqlcommond = MysqlCommond()
mysqlcommond.connectMysql()
mysqlcommond.enquiry()
mysqlcommond.test('test')

# #把爬取到的每条数据组合成一个字典用于数据库数据的插入
# news_dict = {
#     "time": 2018,
#     "no1": 41,
#     "no2": 42,
#     "no3": 43,
#     "no4": 44,
#     "no5": 45,
#     "no6": 46,
#     "no7": 47
#     }


# mysqlcommond.inputlottery(news_dict)