import requests
API_KEY='48HVW9A257ESCIEN'
url=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SPY&apikey={API_KEY}'

response = requests.get(url)
data = response.json()
print(data)
# print(data['Time Series (Daily)'])


# url = f'https://www.alphavantage.co/query?function=MARKET_STATUS&apikey={API_KEY}'
# r = requests.get(url)
# data = r.json()

# print(data)