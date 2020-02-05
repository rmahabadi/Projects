def Upward_Trend(x):
        fifty_day_sma= df['Close'].rolling(window=50).mean()
        two_hundred_day_sma = df['Close'].rolling(window=200).mean()
        fifty_day_sma.dropna(inplace=True)
        two_hundred_day_sma.dropna(inplace=True)
        df10=fifty_day_sma.to_frame().reset_index()
        df2=two_hundred_day_sma.to_frame().reset_index()
        df1 = pd.DataFrame({
            'Date': df10['Date'],
            '50-day-MA': df10['Close'],
            '200-day-MA': df2['Close']})
        if df1.at[i,'50-day-MA']>= df1.at[i,'200-day-MA']:
            print("True Upward Trend")
            increased_volume(df)
        else:  
            print("False No Upward Trend")
def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg
def increased_volume(x):
    if cal_average(df['Volume'][0:10])/cal_average(df['Volume'][10:20])>=1.5:
        print("True increased volume", df['Volume'][0:10])/cal_average(df['Volume'][10:20])
        Repeat(df['High'])
    else:
        print("False no increased volume")

def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j]: 
                repeated.append(x[i]) 
    return repeated 
    Double_top(repeated)
def Double_top(x):
    three_day_high= df['High'][0:3].max()
    time_frame= df['High']
    for i in range(0,30):
        if three_day_high < time_frame[i]:
            continue
        else:
            print(time_frame[i])
            break

def Run_Statistics(x):
    Statistics['Mean']=mean(Repeat(df['High']))
    Statistics['Median']=median(Repeat(df['High']))
    Statistics['Min']=min(Repeat(df['High']))
    Statistics['High']=max(Repeat(df['High']))

def Sideways_Channel(x):
    Consolidation_Top = df['High'][0:30].max()
    Consolidation_Bottom= df['Low'][0:30].min()
    for i in range(30,60):
        if Consolidation_Top == df['High'][i]:
            print(True)
# need to figure out a way to do a plus or minus 5-10% 
#potential code:
# code only accounts for the max of previous highs 
# printed the function to the 
def Sideways_Channel(x):
    Consolidation_Top = df['High'][0:15].max()
    Consolidation_Bottom= df['Low'][0:15].min()
    for i in range(15,60):
        Leeway_High = .15
        Leeway_Low= -.15
        Percent_Comparison = ((Consolidation_Top- df['High'][i])/df['High'][i])
        if (Percent_Comparison >= Leeway_Low) | (Percent_Comparison <= Leeway_High):
            print(Percent_Comparison)
        else:
            break
# formula for change is current minus prior divided by prior

import pandas as pd
import pandas_datareader as dr
from matplotlib import pyplot
%matplotlib inline
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
    df= df.iloc[::-1]
    Upward_Trend(df)