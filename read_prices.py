import pandas_datareader as web
import datetime as dt
import pandas as pd

def crypto(x):
    start = dt.datetime(2020,1,1)
    end = dt.datetime.now()

    x = web.DataReader(str(x)+'-USD', 'yahoo', start, end)
    return x

print(crypto('BTC'))
#print(btc)