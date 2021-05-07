#0xc2edad668740f1aa35e4d8f227fb8e17dca888cd

import requests


import xlrd
r = 0
c = 0
rows = 317
book = xlrd.open_workbook('sushiliqdata.xlsx')
sheet = book.sheet_by_name('Sheet1')
from_ = [sheet.cell_value(r, 0) for r in range(rows)]
to_ = [sheet.cell_value(r, 1) for r in range(rows)]
amount = [sheet.cell_value(r, 2) for r in range(rows)]

count = 0
count_percent = 0
pool_size = 800000000
supply = 0.020529905215212
addr_list = []

for i in range (rows):
    count = count + amount[i]
    if amount[i] > 0.0001:
        print (amount[i])
        print(from_[i])
        addr_list.append(str(from_[i]))
        count_percent = count_percent + (amount[i]/supply * 100)
       # print((amount[i]/supply) * 100, from_[i])
        

print (count)
print (count_percent)

addr_set = set(addr_list)
print (len(addr_set))
    
