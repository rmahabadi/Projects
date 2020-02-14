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
    if cal_average(df['Volume'][79:89])/cal_average(df['Volume'][69:79])>=1.5:
        print("True increased volume", df['Volume'][79:89])/cal_average(df['Volume'][69:79])
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
def Double_top(x):
    three_day_high= df['High][0:3].max()
    time_frame= df[0:30]
    if three_day_high < time_frame['High']:
        print(False)
        else:
            print(True)
#use counter to account for how many times the high is touched (arbitrary number as the charter has to choose, for simplicity sake use 3)
#have to change in case it breaks past parameters 
def Sideways_Channel(x):
    Consolidation_Top = df['High'][0:15].max()
    Consolidation_Bottom= df['Low'][0:15].min()
    for i in range(15,60):
        Leeway_High = .15
        Leeway_Low= -.15
        Percent_Comparison = ((Consolidation_Top- df['High'][i])/df['High'][i])
        if (Percent_Comparison >= Leeway_Low) & (Percent_Comparison <= Leeway_High):
            print(Percent_Comparison)
        else:
            break
# find a way to pass through the consolidation i points in Sideways_Channel to search between those parameters for Higher-highs
def bullish_pattern(Higher_highs):
    Anchor =df['Low'][10:45].min()
    Series=[]
    #series will hold the data of when the delta is negative 
    for i in range(10,45):
        Test=((df['Low'][i]-df['Low'][i-1])/df['Low'][i-1])
        if Anchor < df['Low'][i]:
            print(True)
        if Test < 0:
            Series.append(df['Low'][i])
        # this function will append the period of transition of deltas previous lows to Series for further analysis
        #What still needs to be completed is to run the analysis on the Series data to see if it meets parameteres
