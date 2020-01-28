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
    # might not need this, but not 100% sure
    Double_top(repeated)
    #Run_Statistics(df)
def Double_top(x):
    three_day_high= df['High][0:3].max()
    time_frame= df[0:30]
    if three_day_high < time_frame['High']:
        print(False)
        else:
            print(True)

    
