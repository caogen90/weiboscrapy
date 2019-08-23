# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:27:25 2019

@author: caogen90
"""


import requests
from bs4 import BeautifulSoup
import time
import csv
import re

def getLastPage():
    cookie = '''ALF=1564646277; _T_WM=dcc9bad7024684eaee0c849b1af15764; SUHB=0S7zSt8WVzmjMp; SCF=Aj4RvQJMkmB4iIufuP6VeZaZJDCuB-aOYF_gXn95YUUQ1kBujjl62cu08zA66jeIQefIvsxjd7FK6sI-aFCPaeY.; SUB=_2A25wH2Z4DeRhGedG61UX8SvIzj2IHXVT4AowrDV6PUJbkdAKLWX2kW1NUZVdNBYwM27v3-9VilySyht9xHFq1hT-; SSOLoginState=1562056232'''
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': cookie}
    searchword='%E6%AD%A6%E5%99%A8'
    url = 'https://weibo.cn/search/user/?keyword='+searchword+'&page=1'
    wbdata = requests.get(url,headers=header).text
    soup = BeautifulSoup(wbdata,'lxml')
    inputlst=soup.find('input',{'name':'mp'}).attrs
    lastpage=int(inputlst['value'])
    return (searchword,lastpage)

def getHTMLText():
    abc=getLastPage()
    cookie = '''ALF=1564646277; _T_WM=dcc9bad7024684eaee0c849b1af15764; SUHB=0S7zSt8WVzmjMp; SCF=Aj4RvQJMkmB4iIufuP6VeZaZJDCuB-aOYF_gXn95YUUQ1kBujjl62cu08zA66jeIQefIvsxjd7FK6sI-aFCPaeY.; SUB=_2A25wH2Z4DeRhGedG61UX8SvIzj2IHXVT4AowrDV6PUJbkdAKLWX2kW1NUZVdNBYwM27v3-9VilySyht9xHFq1hT-; SSOLoginState=1562056232'''
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Connection': 'keep-alive',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cookie': cookie}
    csvFile = open('/Users/caogen90/Desktop/爬虫/'+'wuqi.csv','w+',newline='',encoding='gb18030')
    writer = csv.writer(csvFile)
    for i in range(1,abc[1]+1):
        weburl='https://weibo.cn/search/user/?keyword='+abc[0]+'&page='+str(i)
        r=requests.get(weburl,headers=header)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        time.sleep(2)
        soup = BeautifulSoup(r.text, 'html.parser')
        td=soup.find_all('td',{'valign':'top'})
        for j in td:
            if j.find('input') is not None:
                #print(j,'0000000000')
                href=j.a['href']
                #print(href,"111111111")
                text=j.a.get_text()
                #print(text,'222222222')
                alltext=j.get_text()
                p=re.compile('粉.*人')
                fensi=p.findall(alltext)
                #print(fensi,"55555555555")
                kongge=re.split('\xa0',alltext)
                diqu=kongge[1]
                if j.find('img') is not None:
                    dav=j.img['alt']
                    #print(dav,'33333333')
                    davsrc=j.img['src']
                    #print(davsrc,'4444444444')
                    writer.writerow((href,text,dav,davsrc,fensi[0],diqu))
                else:
                    writer.writerow((href,text,'','',fensi[0],diqu))
    csvFile.close
               
        

def main():
    getHTMLText()

main()