from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from coinmarketcapapi import CoinMarketCapAPI, CoinMarketCapAPIError

from datetime import datetime

sample_transport=RequestsHTTPTransport(
    url='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2',
    verify=True,
    retries=3,
)
client = Client(
    transport=sample_transport
)


large_amount = 1000
first_amount = 1000
skip_amount = 1000
token_tx_id = ""
token_name = "BOND"


cmc = CoinMarketCapAPI('6c43df37-3c8e-4875-8b24-bb98bd3e21dd') # Sandbox environnement

try:
    r = cmc.cryptocurrency_quotes_latest(symbol=token_name)
except CoinMarketCapAPIError as e:
    r = e.rep



print("uniswap_analysis.1.0")
print("Current price: $" + (repr (r.data[token_name]['quote']['USD']['price'])))

token_price = (r.data[token_name]['quote']['USD']['price'])


#Important!!! PAIR
pair = "0x6591c4bcd6d7a1eb4e537da8b78676c1576ba244"



barn_in = 0
barn_out = 0
average_usd = 0
txcount_ = 0
txcount_buy = 0
whale_inflow = 0
whale_outflow = 0

loops = 0

while loops < 5:
    i = first_amount-1
    query = gql('''
    query {
      swaps(skip: ''' + str(loops * 1000) + ''', first: 1000, where: { pair: "''' + pair + '''" } orderBy: timestamp, orderDirection: desc) {
          transaction {
            timestamp
          }
          
          amount0In
          amount0Out
          amount1In
          amount1Out
          amountUSD
          to
          sender
        }
    }
    ''')

    response = client.execute(query)



    while i > 0:
        inflow = response['swaps'][i]
        ts = (int(response['swaps'][i]['transaction']['timestamp']))
       
        

        inflow_select = response['swaps'][i]['amount0Out'] # can change
        outflow_select = response['swaps'][i]['amount0In'] # can change 

        barn_in = int(float(response['swaps'][i]['amount0Out'])) + barn_in # can change
        barn_out = int(float(response['swaps'][i]['amount0In'])) + barn_out # can change

        if int((float(outflow_select))) > large_amount:
               whale_outflow = int(float(response['swaps'][i]['amountUSD'])) + whale_outflow
               print("SOLD")

               print (str(int((float(outflow_select)))) + " "+ "$" + token_name + " ---------> "
               + str(int(float(response['swaps'][i]['amountUSD'])))
               + " USD" 

               + " | " +
               (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')))

               
               txcount_ = txcount_ + 1
        
        #print (inflow_select + " "+ token_name )
        if int((float(inflow_select))) > large_amount:
            

            average_usd = int(float(response['swaps'][i]['amountUSD']) / (float(inflow_select))) + average_usd
            txcount_buy = txcount_buy + 1
            whale_inflow = int(float(response['swaps'][i]['amountUSD'])) + whale_inflow
            
            print (response['swaps'][i]['to'])
            
            #print (str(int((float(inflow_select)))) + " "+ "$" + token_name + " ---------> "
            #   + str(int(float(response['swaps'][i]['amountUSD'])))
            #   + " USD" +
            #   " @ " + (str(int(float(response['swaps'][i]['amountUSD']) / (float(inflow_select))))) + " USD" 

            #   + " | " +
            #   (datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')))
            
        i = i-1

    loops = loops + 1

#print(barn_in)
#print(barn_out)
#DELTA
print()
print(str(int(barn_in * (average_usd / txcount_))) + " " + "USD $BOND IN") #USD BARN INFLOW
print()
print(str(whale_inflow) + " " + "USD $BOND WHALE INFLOW") #USD WHALE INFLOW
print(str(whale_outflow) + " " + "USD $BOND WHALE OUTFLOW") #USD WHALE OUTFLOW

print(str(average_usd / txcount_) + " " + "USD $BOND WHALE Average Purchase Price") #WHALE PP

print(str(txcount_) + "  " + "WHALE TRANSACTIONS > 1000 $BOND") #WHALE TX COUNT
print()
print(str(int((barn_in - barn_out) * (average_usd / txcount_buy))) + " " + "USD $BOND NET INFLOW") #USD NET INFLOW


                          


