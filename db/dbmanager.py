# -*- coding: utf-8 -*-
import mysql.connector

class MysqlCommond(object):
    def __init__(self):
        self.user='root'
        self.password="password"
        self.db="lottery"

	# 链接数据库
    def connectMysql(self):
        try:
            self.conn = mysql.connector.connect(user=self.user, passwd=self.password, db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')

    def enquiry(self):
        cursor = self.conn.cursor()
        cursor.execute('select * from testlottery')
        values = cursor.fetchall()
        print (values)
        cursor.close()

    def inputlottery(self,my_dict):
        cursor = self.conn.cursor()
        cols = ', '.join('%s' %id for id in my_dict.keys())
        values = '"," '.join('%s' %id for id in my_dict.values())
        sql = "INSERT INTO testlottery (%s) VALUES (%s)" % (cols, '"' + values + '"')
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()

    def test(self,n):
        print(n)

    def closeCnn(self):
        self.conn.close()

