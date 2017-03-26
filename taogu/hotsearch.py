# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def hotsearch():
    url = 'https://www.taoguba.com.cn/hotPop'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
    source_code = requests.get(url,headers)
    plain_text = source_code.text
    file_content = ''
    result = 'result.txt'
    soup = BeautifulSoup(plain_text,'html.parser')
    tables = soup.find_all('table',id="T2",limit = 2)
    for table in tables:
        for content in table.find_all('span',{'class':'tbleft'}):
            code = content.find('a').get('href')[-6:]
            name = content.find('a').string
            if code not in file_content:
                file_content += "%s\t%s\n"%(code,name)
    f = open(result,'w')
    f.write(file_content)
    f.close()

hotsearch()