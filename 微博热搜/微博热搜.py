# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:34:01 2020

@author: 丁敏
"""

import requests
import bs4


def open_url(url):
    #获取url的信息
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.37 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.37'}
    res = requests.get(url, headers = headers)
    return res



def find_info(res):
    soup = bs4.BeautifulSoup(res.text,'html.parser') #html解析器来解析res获取的数据
    target=soup.find_all('a',target="_blank")
    for each in target[1:50]:
        print(each.text)
 
       
def main():
    url = 'https://s.weibo.com/top/summary'
    res = open_url(url)
    find_info(res)
    
if __name__ == "__main__":
    main()