#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')


file_name = 'kuwo_list.txt'
file_content = ''
file_content += '生成时间:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\n'

def music_spider(name):
    global file_content,file_name
    count = 1
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}
    url = 'http://www.kuwo.cn/bang/content?name=%s' % name
    file_content += name+'\n'
    source_code = requests.get(url, headers=headers)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    list_music = soup.find('ul',{'class':'listMusic'})
    for music_info in list_music.find_all('div',{'class':'name'}):
        tittle = music_info.find('a').string
        href = music_info.find('a').get('href')
        file_content += "%d.%s\t%s\n"%(count,tittle,href)
        count += 1

if __name__ == "__main__":
    list_name = {'酷我新歌榜','酷我飙升榜','酷音乐流行榜','酷我华语榜','网络神曲榜'}
    for name in list_name:
        music_spider(name)
        f = open(file_name,'w')
        f.write(file_content)
        f.close()
