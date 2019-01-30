#-- codng:utf-8 --
import requests
import re
from bs4 import BeautifulSoup
import os 
from io import BytesIO
from saveVideo import SaveVideo


saveV = SaveVideo()

url1 = 'https://media.w3.org/2010/05/sintel/trailer.mp4'
url2 = 'https://media.w3.org/2010/05/sintel/trailer.mp4'
url3 = 'https://media.w3.org/2010/05/sintel/trailer.mp4'

saveV.startLoadVideos([url1,url2,url3],'/Users/haibin.yuan.o/Desktop/Video/test/','test.mp4')



