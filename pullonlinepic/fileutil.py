# -*- coding: utf-8 -*-
import os 

class fileUtil(object):

    def createfile(self):
        a = os.path.abspath('fileutil.py')
        print(a)
        #/Users/haibin.yuan.o/Desktop/python/fileutil.py

        b = os.path.dirname(a)
        print(b)
        #/Users/haibin.yuan.o/Desktop/python

        c = os.path.join(b,'images/')
        print(c)
        #/Users/haibin.yuan.o/Desktop/python/images/ 此时仅仅是路径名，尚未生成真实文件夹

        d = os.path.isdir(c)

        if d:
            print('1')
            pass
        else:
            print('2')
            os.mkdir(c)

        e = os.path.isdir(c)
        print(e)
        return c





