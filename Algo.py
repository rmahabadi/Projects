import pandas as pd
import pandas_datareader as dr
from matplotlib import pyplot
#%matplotlib inline
from datetime import datetime   
import urllib.request
from bs4 import BeautifulSoup
import requests
import re
import datetime
from statistics import mean,median,mode

Ticker=[]
Symbol=[]
Alphavantage_API=[]

for i in range(11,21,10):
    #Skipped first page due to format difference in URL after first page
    Top_Gainers_URL= 'https://finviz.com/screener.ashx?v=340&s=ta_topgainers&r='+str(i)
    r= requests.get(Top_Gainers_URL)
    data=r.text
    soup=BeautifulSoup(data,features="lxml")
    for tickers in soup.find_all('td',attrs={'class':'snapshot-td'}):
        if tickers.find(attrs={'target':'_blank'}) == None:
            for name in tickers.find_all(attrs={'class':'tab-link'}):
                tick = name.text
                s = re.findall("([A-Z]{2,4})", tick)
                for word in s:
                    if word != "USA":
                        Ticker.append(word)

alpha= "https://www.alphavantage.co/query?"
daily = "function=TIME_SERIES_DAILY&"
output = "outputsize=compact&"
api = "apikey=************"

for i in range(0,10):
    symbol.append("symbol=" + Ticker[i] + "&")
    Alphavantage_API.append(alpha+daily+symbol[i]+output+api)
    print(Ticker[i])
    df = dr.data.get_data_yahoo(Ticker[i],start='2015-01-01', end= '2020-01-01')
    Upward_Trend(df)