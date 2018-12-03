# -*- coding: utf-8 -*-
from fileutil import fileUtil

from request import requstPic

filet = fileUtil()

requestpic = requstPic()

a = filet.createfile()

requestpic.download(a)



