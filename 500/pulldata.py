#-- codng:utf-8 --
import requests
import re
from bs4 import BeautifulSoup
from db.dbmanager import MysqlCommond

mysqlcommond = MysqlCommond()
mysqlcommond.connectMysql()

r = requests.get('http://datachart.500.com/dlt/history/newinc/history.php?limit=50&sort=0') 

soup = BeautifulSoup(r.text, 'html.parser')

a = soup.select('#tdata')

b = a[0]

c = b.select('.t_tr1')

d = c[0]

e = d.select('td')

f = e[0]



for x in e:
	print(x.get_text())
	#把爬取到的每条数据组合成一个字典用于数据库数据的插入
    news_dict = {
        "time": 2018,
        "no1": 41,
        "no2": 42,
        "no3": 43,
        "no4": 44,
        "no5": 45,
        "no6": 46,
        "no7": 47
    }


mysqlcommond.inputlottery(news_dict)




