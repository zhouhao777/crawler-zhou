# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import random
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def onetime():
    timenow = int(time.time())
    parm = str(timenow) + str(random.randint(100,999))
    # print parm
    url = 'https://www.taoguba.com.cn/getNrntActualMatch?_='+ parm
    print url
    # 1490547079568
    # 1490547111327


    # headers = [
    # {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
    # {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    # {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    # {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
    # {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
    # {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},
    # {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
    # ]
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
               'Accept':'application/json, text/javascript, */*; q=0.01',
               'Accept-Encoding':'gzip, deflate, sdch, br',
               'Accept-Language':'zh-CN,zh;q=0.8',
               'Connection':'keep-alive',
               'Host':'www.taoguba.com.cn'
               }
    source_code = requests.get(url,headers)
    plain_text = source_code.text
    file_content = ''
    result = 'onetime.txt'
    soup = BeautifulSoup(plain_text,'html.parser')
    lines = soup.find_all('li',{'class':'mu103'})
    print lines
    for line in lines:
        for label in line.find_all('label'):
            name = label.string
            print name
    #         if code not in file_content:
    #             file_content += "%s\t%s\n"%(code,name)
    # f = open(result,'w')
    # f.write(file_content)
    # f.close()

onetime()