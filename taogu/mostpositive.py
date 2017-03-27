# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import random
import time
import json
import re
import MySQLdb
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


def onetime():
    timenow = int(time.time())
    parm = str(timenow) + str(random.randint(100,999))
    url = 'https://www.taoguba.com.cn/getNrntActualMatch?_='+ parm
    
    # headers = [
    # {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
    # {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    # {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    # {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
    # {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
    # {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'},
    # {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
    # ]
    headers = {
               # 'Cookie':'JSESSIONID=f1c29c72-8243-4c7d-bc23-dd6c97baa507; UM_distinctid=15b0d95ad6733e-00b37316d7bbfb-1c3b6b51-1fa400-15b0d95ad68930; CNZZDATA1574657=cnzz_eid%3D1105896313-1490579697-%26ntime%3D1490579697',
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
               }
    source_code = requests.get(url,headers)
    data = json.loads(source_code.text)
    print data['_t']
    print data['status']
    result = {}
    for item in data['dto']['listTopic']:
        res = re.findall(r"\"(.+?)\"",item['recomStock'])
        for onedata in res:
            if result.has_key(onedata):
                result[onedata] += 1
            else:
                result[onedata] = 1
    formatdata = sorted(result.items(), key = lambda x:x[1],reverse=True)
    print type(formatdata)
    return formatdata


def InsertData(dict):
    try:
        conn=MySQLdb.connect(host='localhost',user='root',passwd='ceshi123',db='stock',port=3306)
        cur=conn.cursor()
        for (key,values) in dict:
            cur.execute('insert into hotstock (code,times) values (%s,%s)',(key,values))
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])




# format_data('["sz002302","sh600425","sz000877"]_[268335,268333,268334]')




    # print plain_text
    # file_content = ''
    # result = 'onetime.txt'
    # soup = BeautifulSoup(plain_text,'html.parser')
    # lines = soup.find_all('li',{'class':'mu103'})
    # print lines
    # for line in lines:
    #     for label in line.find_all('label'):
    #         name = label.string
    #         print name
    #         if code not in file_content:
    #             file_content += "%s\t%s\n"%(code,name)
    # f = open(result,'w')
    # f.write(file_content)
    # f.close()

# onetime()
InsertData(onetime())