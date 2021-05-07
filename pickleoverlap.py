import requests


import xlrd
r = 0
c = 0
rows = 88
book = xlrd.open_workbook('badgerdata.xlsx')
sheet = book.sheet_by_name('Sheet1')
addresses = [sheet.cell_value(r, 0) for r in range(rows)]

#print(data)

i = 0
count = 0
while i < rows:
    response_0 = requests.get("https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e&address=" + addresses[i] + "&tag=latest&apikey=A9WI2TYTDM7PY5EDS9Q4NH9NHZN3YX1FBH")
    response_1 = requests.get("https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0x5dbcf33d8c2e976c6b560249878e6f1491bca25c&address=" + addresses[i] + "&tag=latest&apikey=A9WI2TYTDM7PY5EDS9Q4NH9NHZN3YX1FBH")
    response_2 = requests.get("https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress=0xacd43e627e64355f1861cec6d3a6688b31a6f952&address=" + addresses[i] + "&tag=latest&apikey=A9WI2TYTDM7PY5EDS9Q4NH9NHZN3YX1FBH")

    response_0_ = (response_0.json())
    response_1_ = (response_1.json())
    response_2_ = (response_2.json())

    #print(response_0_['result'])


    if int(response_0_['result']) > 0 or int(response_1_['result']) > 0 or int(response_2_['result']) > 0:
        count = count + 1
    
        
    i = i + 1
    print (count)
    



