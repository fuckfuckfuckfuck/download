// sqlite
require("RSQLite")
require("xts")
require("data.table")

m <- dbDriver("SQLite")
con <- dbConnect(m ,dbname = "D:\\bin\\pyproject\\ctpdata\\ctp_20150413.db")
options(stringsAsFactors = FALSE)
Sys.setenv(TZ="GMT")

date = 20150413
id_str = "ag1406"
s1 <- "select * from mktinfo where tradingday = "
s2 <- " and instrumentid = "
s3 <- " and LastPrice <= upperlimitprice and LastPrice >= lowerlimitprice and "
s4 <- "(substr(updatetime,1,5) <= "02:30" or (substr(updatetime,1,5) >= \"08:55\" and substr(updatetime,1,5) <= \"15:15\") or substr(updatetime,1,5) >= \"20:55\" );"
s5 <- " order by updatetime,updatemillisec ;"
\"ag1506\" ;"
sql <- 20150413
rs <- dbSendQuery(con, sql)
data <- fetch(rs, n = -1)

dbClearResult(rs)
dbDisconnect(con)



