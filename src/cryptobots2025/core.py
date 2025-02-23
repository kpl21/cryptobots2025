from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
from dotenv import load_dotenv
from json import dumps

from coinbase.rest import RESTClient

# Load environment variables from .env file
load_dotenv()

#coinbase stuff
coinbase_api_key = os.getenv('COINBASE_API_KEY')
coinbase_api_secret=os.getenv('COINBASE_API_SECRET')

client = RESTClient(api_key=coinbase_api_key, api_secret=coinbase_api_secret)

accounts = client.get_accounts()
data = (dumps(accounts.to_dict(), indent=2))

with open("../../data/accounts.json", 'w') as file:
    json.dump(data, file, indent=4)


# coinmarketcap stuff
# Get API key
# api_key = os.getenv('API_KEY')

# url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
# parameters = {
#   'slug':'solana',

# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': api_key
#   }

# session = Session()
# session.headers.update(headers)

# try:
#   response = session.get(url, params=parameters)
#   data = json.loads(response.text)
#   print(data['data']['5426']['quote'])
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)