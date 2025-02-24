import os
from dotenv import load_dotenv

from coinbase.rest import RESTClient

class Order:
    price: float
    size: float
    side: str  # 'bid' or 'ask'
    timestamp: float = None

# Load environment variables from .env file
load_dotenv()

#coinbase stuff
coinbase_api_key = os.getenv('COINBASE_API_KEY')
coinbase_api_secret=os.getenv('COINBASE_API_SECRET')

client = RESTClient(api_key=coinbase_api_key, api_secret=coinbase_api_secret)

product = client.get_product_book("SOL-USD", limit=100)

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
                side='bid',
                timestamp=time.time()
            )
            for ask in asks
        ]

print(bid_orders)
print(ask_orders)

