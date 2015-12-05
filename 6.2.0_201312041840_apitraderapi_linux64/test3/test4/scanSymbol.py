# -*- coding: utf-8 -*- 
import sqlite3
import re

line1 = "IF1603|SHFE|IF1603|IF1603|IF|1|2016|3|50|1|100|1|300|0.2|20150706|20150720|20160318|20160318|20160318|1|1|2|1|0.4|0.4|1"
symbol_pattern ="(\w+)\|([a-zA-Z]+)\|\S+\|(\w+)\|([a-zA-Z]+)\|(\w+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+\.?\d*)\|(\w+)\|(\w+)\|(\w+)\|(\w+)\|(\w+)\|(\w+)\|(\d+)\|(\w+)\|(\w+)\|(\d+\.?\d*)\|(\d+\.?\d*)\|(\w+)"
ps = re.compile(symbol_pattern)
# fstrm << pInstrument->InstrumentID<<'|'<<pInstrument->ExchangeID <<'|'<<pInstrument->InstrumentName <<'|'<<pInstrument->ExchangeInstID <<'|'<<pInstrument->ProductID <<'|'<<pInstrument->ProductClass <<'|'<<pInstrument->DeliveryYear <<'|'<<pInstrument->DeliveryMonth <<'|'<<pInstrument->MaxMarketOrderVolume <<'|'<<pInstrument->MinMarketOrderVolume <<'|'<<pInstrument->MaxLimitOrderVolume <<'|'<<pInstrument->MinLimitOrderVolume <<'|'<<pInstrument->VolumeMultiple <<'|'<<pInstrument->PriceTick <<'|'<<pInstrument->CreateDate <<'|'<<pInstrument->OpenDate <<'|'<<pInstrument->ExpireDate <<'|'<<pInstrument->StartDelivDate <<'|'<<pInstrument->EndDelivDate <<'|'<<pInstrument->InstLifePhase <<'|'<<pInstrument->IsTrading <<'|'<<pInstrument->PositionType <<'|'<<pInstrument->PositionDateType <<'|'<<pInstrument->LongMarginRatio <<'|'<<pInstrument->ShortMarginRatio <<'|'<<pInstrument->MaxMarginSideAlgorithm << endl;

sql_0 = "create table if not exists symbols (InstrumentID TEXT,ExchangeID TEXT, InstrumentName TEXT, ExchangeInstID TEXT, ProductID TEXT, ProductClass TEXT, DeliveryYear INT, DeliveryMonth INT, MaxMarketOrderVolume INT, MinMarketOrderVolume INT, MaxLimitOrderVolume INT, MinLimitOrderVolume INT, VolumeMultiple INT, PriceTick DOUBLE, CreateDate TEXT, OpenDate TEXT, ExpireDate TEXT, StartDelivDate TEXT, EndDelivDate TEXT,InstLifePhase TEXT, IsTrading INT, PositionType TEXT, PositionDateType TEXT, LongMarginRatio DOUBLE, ShortMarginRatio DOUBLE, MaxMarginSideAlgorithm TEXT, primary key (InstrumentID));"

sql_1 = "insert into symbols (InstrumentID ,ExchangeID , ExchangeInstID , ProductID , ProductClass , DeliveryYear , DeliveryMonth , MaxMarketOrderVolume , MinMarketOrderVolume , MaxLimitOrderVolume , MinLimitOrderVolume , VolumeMultiple , PriceTick , CreateDate , OpenDate , ExpireDate , StartDelivDate , EndDelivDate ,InstLifePhase , IsTrading , PositionType , PositionDateType , LongMarginRatio , ShortMarginRatio , MaxMarginSideAlgorithm ) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?); "

con = sqlite3.connect("tickers.db")
cur = con.cursor()

# def process():
    # try:
    #     cur.execute(sql_0)
    # except sqlite3.Error as e:
    #     print("failed to create table, %s.\n" % e.args[0])
    # else:
    #     con.commit()

fstr = open("symbols.txt",'r')
lines = fstr.readlines()
print(len(lines))
for line in lines:
    tmp = ps.match(line)
    if (tmp is not None):
        try:
            cur.execute(sql_1,tmp.groups())
        except sqlite3.Error as e:
            print("Failed insertion, %s" % e.args[0])
    else:
        print("failed insertion,%s" % line)
        pass

con.commit()
fstr.close()
cur.close()
con.close()
con == None






