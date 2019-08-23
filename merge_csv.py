# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:26:57 2019

@author: caogen90
"""

import os
import pandas as pd
import glob
 
#定义函数hebing
 
def hebing():
    csv_list = glob.glob('*.csv') #查看同文件夹下的csv文件数
    print(u'共发现%s个CSV文件'% len(csv_list))
    print(u'正在处理............')
    for i in csv_list: #循环读取同文件夹下的csv文件       
        fr = open(i,'r',encoding='utf-8').read()
        with open('result.csv','a') as f: #将结果保存为result.csv
            f.write(fr)
    print(u'合并完毕！')
 
#定义函数quchong(file)，将重复的内容去掉，主要是去表头
 
def quchong(file):
    df = pd.read_csv(file,header=0)
    datalist = df.drop_duplicates()
    datalist.to_csv(file)

#运行函数
if __name__ == '__main__':
    hebing()
    quchong("result.csv")