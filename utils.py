def readData(fn, mode = 'r'):
    FH = open(fn, mode)
    data = FH.read()
    FH.close()
    return data

def writeData(fn, data, mode = 'w'):
    FH = open(fn, mode)
    FH.write(data)
    FH.close()

def chunks(s, n=2):
    rL = list()
    while s:
        rL.append(s[:2])
        s = s[2:]
    return rL
