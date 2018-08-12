import json
import requests


url = "https://api.coinmarketcap.com/v2/ticker"
resp = requests.get(url)
data = json.loads(resp.text)

btc = data['data']['1']
print(btc['quotes']['USD'])