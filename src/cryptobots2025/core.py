import os
from dotenv import load_dotenv
import time
from order import Order
from coinbase.rest import RESTClient
import csv

# Load environment variables from .env file
load_dotenv()

#coinbase stuff
coinbase_api_key = os.getenv('COINBASE_API_KEY')
coinbase_api_secret=os.getenv('COINBASE_API_SECRET')

client = RESTClient(api_key=coinbase_api_key, api_secret=coinbase_api_secret)

product = client.get_product_book("SOL-USD")

pricebook = product.pricebook

bids = pricebook.bids # list of dictionaries
asks = pricebook.asks # list of dictionaries
# print(bids)
# print(asks)
bids_orders = [
            Order(
                price=bid['price'],
                size=bid['size'],
                side='bid',
                timestamp=time.time()
            )
            for bid in bids
        ]
asks_orders = [
            Order(
                price=ask['price'],
                size=ask['size'],
                side='ask',
                timestamp=time.time()
            )
            for ask in asks
        ]

bids_orders.sort(key=lambda x: x.price, reverse=True) # Highest buy prices first
asks_orders.sort(key=lambda x: x.price) # Lowest sell prices first

for order in bids_orders:
    print("\033[31m" + str(order) + "\033[0m")

for order in asks_orders:
    print("\033[32m" + str(order) + "\033[0m")


csv_file = '../../data/orderbook.csv'

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for order in bids_orders:
        writer.writerows(str(order.side) + "," + str(order.price) + "," + str(order.size) + "," + str(order.timestamp))
    for order in asks_orders:
        writer.writerows(str(order.side) + "," + str(order.price) + "," + str(order.size) + "," + str(order.timestamp))

