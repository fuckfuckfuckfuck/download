import sys
import re


#~ config = {
    #~ 'user' : 'botel',
    #~ 'password': '12345678',
    #~ 'database' : 'mktinfo',
    #~ 'host' : 'rdsryfjb2vqrni2.mysql.rds.aliyuncs.com',
    #~ 'charset' : 'utf8',
    #~ 'raise_on_warnings' : True
#~ }

Handler = {
    'user' : str,
    'password' : str,
    'database' : str,
    'host' : str,
    'charset' : str,    
    'port' : str,
    'raise_on_warnings' : bool
}

dir = '/home/dell/Downloads/6.2.0_201312041840_apitraderapi_linux64/test3/test4/'

def scanParam(fileStr):
	#~ reader = open(sys.argv[1], 'r')
    # fileStr = dir + fileStr
    reader = open(fileStr,'r')
    param = {}
    for line in reader:
		tmp = re.search('[%\[\]]',line) #
		if tmp:
			print tmp.group()
			continue
		line = line.split('#')[0].strip()
		if not line:
			continue

		name, value = line.split()
		if name not in Handler:
			print >> sys.stderr, 'Bad parameter name "%s"' % name
			sys.exit(1)
		if name in param:
			print >> sys.stderr, 'Duplicate parameter name "%s"' % name
			sys.exit(1)

		conversion_func = Handler[name]
		param[name] = conversion_func(value)

    return param


# file = 'conf'
# scanedParams = scanParam(dir + file)
