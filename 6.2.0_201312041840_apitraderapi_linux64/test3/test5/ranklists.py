
def ranks(file):
    reader = open(file,'r')
    a = []
    for line in reader:
        a.append(line)
    a.sort()
    reader1 = open(file+'.3','w')
    for ii in a:
        reader1.write(ii)
    
    reader.close()
    reader1.close()

ranks("3.txt.1")
