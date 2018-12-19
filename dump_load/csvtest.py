#!/usr/bin/env python3

# 读取文件，用 reader 读取的结果是个迭代器，文件关闭后此迭代器无法读取数据,所以要在关闭文件前处理
import csv
with open('/home/shiyanlou/test.csv','r') as file:
        data = list(csv.reader(file))   #reader方法读取csv文件，并转换为列表模式 
        for i in data:
                print(i)

#  writer data
with open('test_w.csv','w') as f:   
        csv.writer(f).writerows(data)      #读取data列表中数据，并写入到test_w.csv文件中
