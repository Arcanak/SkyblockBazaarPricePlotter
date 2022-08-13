from datetime import date
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import mplfinance as mpf


input = input()
itemName = input

if input == "":
    itemName = 'STOCK_OF_STONKS'

today = date.today()
params = '/history/?start=1970-01-01T00:00:00.000Z&end={today}'.format(today=today.strftime('%Y-%m-%dT%H:%M:%S.000Z'))

url = 'https://sky.coflnet.com/api/bazaar/' + itemName + params

def get_data_json(url):
    response = requests.get(url)
    return json.loads(response.text)


def get_data_df(url):
    response = requests.get(url)
    df = pd.read_json(response.text)
    df.sort_index(ascending=False, inplace=True)
    df.set_index('timestamp')
    return df

df = get_data_df(url)
minBuy = df['minBuy'].values
maxSell = df['maxSell'].values
volume = df['sellVolume'].values + df['buyVolume'].values / 2
timestamp = df['timestamp'].values

plt.figure(figsize=(12,8))
plt.plot(timestamp, minBuy, label='minBuy', color='blue')
plt.plot(timestamp, maxSell, label='maxSell', color='red')
plt.bar(timestamp, volume, label='sellVolume', color='g', alpha=0.3)
plt.yscale('log')
plt.legend()

plt.figure(figsize=(12,8))
plt.plot(timestamp,  1 / minBuy, label='minBuy', color='blue')
plt.plot(timestamp, 1 / maxSell, label='maxSell', color='red')
plt.yscale('log')

plt.show()


#plt.plot(timestamp, np.convolve(price, np.ones(20)/20, mode='same'), label='smoothed price')
#plt.bar(timestamp, volume, label='sellVolume', color='g', alpha=0.3)
#plt.yscale('log')



#plt.show()



