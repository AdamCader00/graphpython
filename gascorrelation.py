import requests
import json

from datetime import datetime

#curve-finance
tvl_0 = requests.get("https://data-api.defipulse.com/api/v1/defipulse/api/GetHistory?period=1m&project=curve-finance&api-key=97ca566dd7e1c518bccd19871b1fa912c2ac05808f0e022c5640c9a866fc")
tvl_1 = requests.get("https://data-api.defipulse.com/api/v1/defipulse/api/GetHistory?period=1m&project=sushiswap&api-key=97ca566dd7e1c518bccd19871b1fa912c2ac05808f0e022c5640c9a866fc")
tvl_2 = requests.get("https://data-api.defipulse.com/api/v1/defipulse/api/GetHistory?period=1m&project=badger-dao&api-key=97ca566dd7e1c518bccd19871b1fa912c2ac05808f0e022c5640c9a866fc")
tvl_3 = requests.get("https://data-api.defipulse.com/api/v1/defipulse/api/GetHistory?period=2m&project=dydx&api-key=97ca566dd7e1c518bccd19871b1fa912c2ac05808f0e022c5640c9a866fc")


tvlnull = requests.get("https://data-api.defipulse.com/api/v1/egs/api/ethgasAPI.json?api-key=97ca566dd7e1c518bccd19871b1fa912c2ac05808f0e022c5640c9a866fc")

data0 = tvl_0.json()
data1 = tvl_1.json()
data2 = tvl_2.json()
data3 = tvl_3.json()

for value in data0:
    #print(value['tvlUSD'])
    dt_obj = datetime.fromtimestamp((value['timestamp']))
    #print(dt_obj)

for value in data1:
    #print(value['tvlUSD'])
    dt_obj = datetime.fromtimestamp((value['timestamp']))
    #print(dt_obj)

for value in data3:
    print(value['tvlUSD'])
    dt_obj = datetime.fromtimestamp((value['timestamp']))
    #print(dt_obj)


