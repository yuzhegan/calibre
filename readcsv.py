# encoding='utf-8

# @Time: 2021-12-14
# @File: %
#!/usr/bin/env
from icecream import ic
import csv
def ReadCsv(csvpath):
    with open(csvpath, 'r') as f:
        datas = csv.reader(f)
        list = []
        for data in datas:
            data = data[0]
            data = eval(data) #to dict
            # print(data)
            list.append(data)
    return list
a = ReadCsv("aopplo.csv")
print (a)

