from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv
from json import dumps
import order
import pandas as pd

from coinbase.rest import RESTClient

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
print(bids)
print(asks)

