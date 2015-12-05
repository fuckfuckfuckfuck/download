import re
import os
import string

# 5467168 [140180629845760] DEBUG test <> - 20151026 au1602   239.5 240.5 240.4 70 241.2 241.2 239.5 6 1.4419e+06 68 1.79769e+308 1.79769e+308 252.5 228.45 01:09:30 0 23


# prepare
## mkt_pattern = "(\d+)\s\[(\d+)\]\s([A-Z]+)\stest\s<>\s-\s(\d+)\s(\w+)\s+(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d\d:\d\d:\d\d)\s(\d+)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.\d*[eE]?[+]?\d*)\s(\d+)"

mkt_pattern = "(\d+)\s\[(\d+)\]\s([A-Z]+)\stest\s<>\s-\s(\d+)\s(\w+)\s+(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d\d:\d\d:\d\d)\s(\d+)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+)"
p = re.compile(mkt_pattern)
def record(res):
    recordss = {
        'id' : res[0],
        'thread' : res[1],
        'loglevel' : res[2], 
        'TradingDay' : res[3],
        'InstrumentID' : res[4],
        'LastPrice' : res[5],
        'PreSettlementPrice' : res[6],
        'PreClosePrice' : res[7],
        'PreOpenInterest' : res[8],
        'OpenPrice' : res[9],
        'HighestPrice' : res[10],    
        'LowestPrice' : res[11],
        'Volume' : res[12],
        'Turnover' : res[13],
        'OpenInterest' : res[14],
        'ClosePrice' : res[15],
        'SettlementPrice' : res[16],
        'UpperLimitPrice' : res[17],
        'LowerLimitPrice' : res[18],
        'UpdateTime' : res[19],
        'UpdateMillisec' : res[20],
        'BidPrice1' : res[21],
        'BidVolume1' : res[22],
        'AskPrice1' : res[23],
        'AskVolume1' : res[24],
        'AveragePrice' : res[25],
        'seq_num' : res[26]
        }
    return recordss


add_record = "INSERT INTO ctp (id,thread, loglevel, TradingDay, InstrumentID, LastPrice, PreSettlementPrice, PreClosePrice, PreOpenInterest, OpenPrice, HighestPrice, LowestPrice, Volume, Turnover, OpenInterest, ClosePrice, SettlementPrice, UpperLimitPrice, LowerLimitPrice, UpdateTime, UpdateMillisec, BidPrice1, BidVolume1, AskPrice1, AskVolume1, AveragePrice, seq_num) VALUES (%(id)s,%(thread)s,%(loglevel)s,%(TradingDay)s,%(InstrumentID)s,%(LastPrice)s,%(PreSettlementPrice)s,%(PreClosePrice)s,%(PreOpenInterest)s,%(OpenPrice)s,%(HighestPrice)s,%(LowestPrice)s,%(Volume)s,%(Turnover)s,%(OpenInterest)s,%(ClosePrice)s,%(SettlementPrice)s,%(UpperLimitPrice)s,%(LowerLimitPrice)s,%(UpdateTime)s,%(UpdateMillisec)s,%(BidPrice1)s,%(BidVolume1)s,%(AskPrice1)s,%(AskVolume1)s,%(AveragePrice)s,%(seq_num)s ) "


def isTestlogFile(fstr):
    fstr = fstr.strip()
    fstr = fstr.split('/')[-1]
    p = re.compile("Test.log[\.\d+]?")
    if (p.match(fstr) != None) and (fstr[-1] != '~'):
        return True
    return False

def findTestlogfiles(dir):
    dirs = dir.strip()
    files = os.listdir(dirs)
    filelist = []
    for f in files:
        ff = string.join((dir,f), '/')
        if (os.path.isfile(ff)) and isTestlogFile(ff):
            if f not in filelist:
                num = re.findall(r'\d+', f)
                if len(num) == 0:
                    num = '0'
                elif len(num) > 0:
                    num = num[0]
                filelist.append({'name' : f, 'num' : int(num)})

    ans = sorted(filelist, key = lambda x : x['num'])
    return [x['name'] for x in ans]




#    recordss = {
#        'id' : int(res[0]),
#        'thread' : int(res[1]),
#        'loglevel' : res[2], 
#        'TradingDay' : int(res[3]),
#        'InstrumentID' : res[4],
#        'Lastprice' : float(res[5]),
#        'PreSettlementPrice' : float(res[6]),
#        'PreClosePrice' : float(res[7]),
#        'PreOpenInterest' : int(res[8]),
#        'OpenPrice' : float(res[9]),
#        'HighestPrice' : float(res[10]),    
#        'LowestPrice' : float(res[11]),
#        'Volume' : int(res[12]),
#        'Turnover' : float(res[13]),
#        'OpenInterest' : int(res[14]),
#        'Closeprice' : float(res[15]),
#        'SettlementPrice' : float(res[16]),
#        'UpperLimitPrice' : float(res[17]),
#        'LowerLimitPrice' : float(res[18]),
#        'UpdateTime' : res[19],
#        'UpdateMillisec' : int(res[20]),
#        'BidPrice1' : float(res[21]),
#        'BidVolume1' : int(res[22]),
#        'AskPrice1' : float(res[23]),
#        'AskVolume1' : int(res[24]),
#        'AveragePrice' : float(res[25]),
#        'seq_num' : int(res[26])
#        }
        
        
