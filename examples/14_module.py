# coding=UTF-8

'''
from mod1 import sum
sum(3, 4)

from mod1 import sum, safe_sum
from mod1 import *
'''

import modules.mod2
print(modules.mod2.PI)

a = modules.mod2.Math()
print(a.solv(2))

# random, urllib 사용
print ''
print '='*5 + 'random, urllib 사용'
import random
import urllib

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_file_name = str(name) + ".jpg"
    urllib.urlretrieve(url, full_file_name)

download_web_image("http://img.naver.net/static/www/u/2013/0731/nmms_224940510.gif")

# x = random.randrange(1, 1000)
# print x