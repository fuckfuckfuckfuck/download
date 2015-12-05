import sqlite3

# create table symbols(symbol TEXT NOT NULL, src TEXT NOT NULL, PRIMARY KEY(symbol, src));
# create table symbols_2(symbol TEXT NOT NULL, src TEXT NOT NULL, date INT, PRIMARY KEY(symbol, src, date));


def processFile(filestr,srcStr, datee):
    try:
        conn = sqlite3.connect("tmpp.db")
    except sqlite3.Error as err:
        print "connect db failed."
        print "Reason: %s" % err.args[0]
        return

    cur = conn.cursor()

    filee = open(filestr, 'r')
    lines = filee.readlines()
    ii = 0
    # re = []
    for line in lines:
        line = line.strip()

        try:
            cur.execute("insert into symbols_2 (symbol, src, date) values(?,?,?);",(line, srcStr, datee))    
            # ++ii
            # print "%s,%s" % (line,ii)
        except sqlite3.Error as err:
            print "failed to insert %s, ret=%s" % (line, err.args[0])

    conn.commit()
    
    filee.close()
    cur.close()
    conn.close()


processFile("3.txt.20150831", "ht_cffe", 20150831)
# processFile("3.txt", "gs_simu")


