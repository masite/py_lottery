# -*- coding: UTF8 -*-
from pyquery import PyQuery as pq
import sys, os
import json
import requests
from contextlib import closing
import time, threading


class SaveVideo():
    LessonList = []

    def __init__(self):
        pass

    # url为传时，则用默认值
    def startLoadVideo(self,url,file_d,file_name):
        if not os.path.exists(file_d):
                os.makedirs(file_d)
        self.downloadVideo(url,file_d,file_name)


    def startLoadVideos(self,urls,file_d,file_name):
        if not os.path.exists(file_d):
                os.makedirs(file_d)

        for index, url in enumerate(urls):

            self.startLoadVideo(url,file_d,str(index)+'temp'+'.mp4')


    def downloadVideo(self, url, file_d, file_name=''):
        file_D = file_d + file_name
        with closing(requests.get(url, stream=True)) as response:
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
            
            if(os.path.exists(file_D)  and os.path.getsize(file_D)==content_size):
                print('跳过'+string(file_name))
            else:
                progress = ProgressBar(file_name, total=content_size, unit="KB", chunk_size=chunk_size, run_status="正在下载",fin_status="下载完成")
                with open(file_D, "wb") as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        progress.refresh(count=len(data))


'''
下载进度
'''
class ProgressBar(object):
    def __init__(self, title, count=0.0, run_status=None, fin_status=None, total=100.0, unit='', sep='/',
                 chunk_size=1.0):
        super(ProgressBar, self).__init__()
        self.info = "[%s] %s %.2f %s %s %.2f %s"
        self.title = title
        self.total = total
        self.count = count
        self.chunk_size = chunk_size
        self.status = run_status or ""
        self.fin_status = fin_status or " " * len(self.statue)
        self.unit = unit
        self.seq = sep

    def __get_info(self):
        # 【名称】状态 进度 单位 分割线 总数 单位
        _info = self.info % (
            self.title, self.status, self.count / self.chunk_size, self.unit, self.seq, self.total / self.chunk_size,
            self.unit)
        return _info

    def refresh(self, count=1, status=None):
        self.count += count
        # if status is not None:
        self.status = status or self.status
        end_str = "\r"
        if self.count >= self.total:
            end_str = '\n'
            self.status = status or self.fin_status
        print(self.__get_info(), end=end_str)


if __name__ == '__main__':
    sys.exit()