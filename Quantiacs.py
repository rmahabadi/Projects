import numpy

def myTradingSystem(DATE, OPEN, HIGH, LOW, CLOSE, VOL, exposure, equity, settings):
    
    nMarkets = CLOSE.shape[1]
    
    candles = 4
    lastcandles = CLOSE[-candles:,:]
    print(lastcandles)
    
    candlesDiff = numpy.diff(lastcandles, axis=0)
    print(candlesDiff)
    
    longEquity = numpy.all(candlesDiff < 0, axis=0)
    print(longEquity)
    
    shortEquity = numpy.all(candlesDiff > 0, axis =0)
    print(shortEquity)
    
    pos=numpy.zeros(nMarkets)
    pos[longEquity] = 1
    pos[shortEquity]= -.5
    print(pos)
    
    return pos, settings


def mySettings():

    settings= {}

    settings['markets'] = ['AAPL','ABT','ABBV']
    settings['beginInSample'] = '20190101'
    settings['endInSample'] = '20200101'
    settings['lookback']= 100
    settings['budget']= 10**6
    settings['slippage']= 0.05

    return settings

    if __name__ == '__main__':
        import quantiacsToolbox
        results = quantiacsToolbox.runts(__file__)