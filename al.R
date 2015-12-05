Sys.setenv(TZ="GMT")
require("xts")
require("quantmod")

dataday  <- function(file,dtime="day") {
  data <- data.frame(read.csv(file=file,header=TRUE))
  if (dtime == "day")
    format_dtime <- "%Y-%m-%d"
  else if (dtime == "min")
    format_dtime <- "%Y-%m-%d %H:%M"
  
  data <- as.xts(data[,-1],order.by=strptime(data[,1],format=format_dtime,tz="GMT"))    
}
datadir <- "d:\\My Documents\\chongyang\\bin\\tbv441_portable\\User\\wangwatercup\\Desktop\\我的工作区\\data\\"
mktcolname <- c("open","high",'low',"close","volume","openint")

rollingstd <- function(data,n) {
  f1 <- function(i) {
    if (i<n)
      re <- 0
    else {
      s0 <- i-n+1
      re <- var(data[s0:i,"close"])
    }
    sqrt(re[1])  
  }
  nrows <- nrow(data) # xts data
  re <- unlist(lapply(seq(1,nrows), f1))  
  re <- xts(re,order.by=index(data),tz="GMT")
}

# pricevolume_realized <- function(xdata) {  
#   cumvol <- sum(xdata[,"volume"],na.rm=T)
#   realsig <- sqrt(sum((diff(xdata[,"close"]))^2,na.rm=T))
#   adj_ret <- diff(xdata[,"close"])/realsig
#   adj_vol <- sqrt(xdata[,"volume"]/cumvol)
# #   re <- cbind(adj_ret,adj_vol,adj_ret/adj_vol)  
#   re <- adj_ret/adj_vol
#   re <- re[complete.cases(re)]
# }
pricevolume <- function(xdata) {   
  re <- diff(xdata[,"close"])/sqrt(xdata[,"volume"])
  re <- as.numeric(re[complete.cases(re)])
}
pricevolume_ratio <- function(min,day,dailystd) {
  tmp <- function(minx) {
#     as.date()
    dates <- strftime(index(minx[1]),format="%Y-%m-%d")
    re <- coredata(dailystd[dates])/coredata(sqrt(day[dates,"volume"]))
    pricevolume(minx)/as.numeric(re)      
  }
  ep <- endpoints(min,"days")
#   re <- period.apply(min,INDEX=ep,tmp)
  unlist(period.apply(min,INDEX=ep,tmp))
}

##########################################
al888min <- dataday(paste(datadir,"min\\al888.csv",sep=""),"min")
al888day <- dataday(paste(datadir,"day\\al888.csv",sep=""),"day")
colnames(al888min) <- mktcolname
colnames(al888day) <- mktcolname
al888min <- al888min["/2014-06-03"]
al888day <- al888day["/2014-06-03"]
save.image(file="AL.RData")
##########################################dailyviews
dailystd <- rollingstd(al888day,23)
pq_ratio <- pricevolume_ratio(al888min["2014-04-01/"],al888day,dailystd)

hist(as.numeric(pq_ratio))
quantile(as.numeric(pq_ratio),probs=seq(0,1,0.05))
plot(as.numeric(pq_ratio))

pqint <- as.integer(pq_ratio/0.02)
hist(pqint)
summary(pqint)
plot(order(pqint))
t = pqint[order(pqint)]
plot(t)
plot(diff(t))
quantile(t,probs=seq(0,1,0.05))
quantile(t,probs=seq(0.45,0.57,0.005))
save.image(file="AL2.RData")

t1 <- if888min["2014-05-27/"]
