from pprint import pprint 
import requests

def do_stocks():
    symbol= input("Enter the market ticker: ")
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+ symbol + "&interval=1min&outputsize=compact&apikey=D6WVP1SOBOAINFVF"
    res = requests.get(url)
    data = res.json()['Time Series (1min)']
    key = list(data.keys())[0]
    for k,v in data[key].items():
        print( k, v)

