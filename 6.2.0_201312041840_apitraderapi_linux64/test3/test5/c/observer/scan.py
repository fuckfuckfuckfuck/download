import re
import os
import string

# line = "18246655 [139707331954432] DEBUG test <> - 20140627 au1408   263.25 264.05 263.8 212 262.45 263.25 262.45 16 4.2072e+06 220 1.79769e+308 1.79769e+308 277.25 250.8 02:00:15 0 262.75 2 263.3 1 262950 255957"

mkt_pattern = "(\d+)\s\[(\d+)\]\s([A-Z]+)\stest\s<>\s-\s(\d+)\s(\w+)\s+(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d\d:\d\d:\d\d)\s(\d+)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+\.?\d*[eE]?[+]?\d*)\s(\d+)"

p_header = "(\d+)\s\[(\d+)\]\s([A-Z]+)\stest\s<>\s-\s"
p_rtnInstrumentStatus = "OnRtnInstrumentStatus\s([A-Z]+)|(\d+)|(\d+)|(\d+):(\d+):(\d+)|(\d+)"
p_rtnOrder = "OnRtnOrder:\s(\w+)|(\d+)|(\d+)|(\d+)|(\d+)|"