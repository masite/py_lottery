# -*- coding: utf-8 -*-
import requests
import re
from PIL import Image
import os 
from io import BytesIO

class requstPic(object):
    def __init__(self):
        super(requstPic, self).__init__()

    def download(self,native_path):
        print(native_path)
        picurl = requests.get("http://pic.yxdown.com/list/0_0_1.html")

        reg = 'src="(.+?\.jpg)"'
        imgre = re.compile(reg)
        imglist = re.findall(imgre, picurl.text)

        ######## 循环下载图片
        for index, val in enumerate(imglist):
            html = requests.get(val)
            img_name = str(index + 1) + '.jpg'
            image = Image.open(BytesIO(html.content))
            image.save(native_path + img_name)
            print('第%d张图片下载完成' % (index + 1))

            print('抓取完成')






