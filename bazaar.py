from datetime import date
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np


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
price = df['minBuy'].values + df['minSell'].values + df['maxSell'].values / 3
volume = df['sellVolume'].values + df['buyVolume'].values
timestamp = df['timestamp'].values

fig, ax = plt.subplots()

plt.plot(timestamp, price, label='price')
plt.plot(timestamp, np.convolve(price, np.ones(20)/20, mode='same'), label='smoothed price')
plt.bar(timestamp, volume, label='sellVolume', color='g', alpha=0.3)
plt.yscale('log')



plt.show()



