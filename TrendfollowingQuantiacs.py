import numpy

def myTradingSystem(DATE,OPEN,HIGH,LOW,CLOSE,VOL,exposure,equity,settings):
    
    nMarkets = CLOSE.shape[1]

    periodLong = 200
    periodShort = 40
    print(CLOSE)
    smaLong = numpy.nansum(CLOSE[-periodLong:,:],axis=0)/periodLong
    smaRecent = numpy.nansum(CLOSE[-periodShort:,:],axis=0)/periodShort

    longEquity = numpy.array(smaRecent > smaLong)
    shortEquity = ~longEquity

    pos = numpy.zeros((1,nMarkets))
    pos[0, longEquity] =1 
    pos[0, shortEquity] = -1

    weights = pos/numpy.nansum(abs(pos))
    return weights, settings

settings={}

def mySettings():

    settings['markets']=['CASH','AAPL','ABBV','ABT','ACN','AEP','AIG','ALL',
    'AMGN','AMZN','APA','APC','AXP','BA','BAC','BAX','BK','BMY','BRKB','C',
    'CAT','CL','CMCSA','COF','COP','COST','CSCO','CVS','CVX','DD','DIS','DOW',
    'DVN','EBAY','EMC','EMR','EXC','F','FB','FCX','FDX','FOXA','GD','GE',
    'GILD','GM','GOOGL','GS','HAL','HD','HON','HPQ','IBM','INTC','JNJ','JPM',
    'KO','LLY','LMT','LOW','MA','MCD','MDLZ','MDT','MET','MMM','MO','MON',
    'MRK','MS','MSFT','NKE','NOV','NSC','ORCL','OXY','PEP','PFE','PG','PM',
    'QCOM','RTN','SBUX','SLB','SO','SPG','T','TGT','TWX','TXN','UNH','UNP',
    'UPS','USB','UTX','V','VZ','WAG','WFC','WMT','XOM']

    settings['beginInSample']= '20170101'
    settings['endInSample'] = '20200101'
    settings['lookback']=300
    settings['budget'] = 10**6
    settings['slippage']= 0.05

    return settings

if __name__ == "__main__":
    import quantiacsToolbox
    results = quantiacsToolbox.runts('/Users/rostammahabadi/Documents/Projects/TrendfollowingQuantiacs.py')
