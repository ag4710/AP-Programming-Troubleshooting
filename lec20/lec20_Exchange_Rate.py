# Read KRW-USD rates
# We have data from 1993 to 2009
years = range(1994, 2010)

# read one year and return list
def read_year(yr):
    fname = "lec20/ExchangeRate/%d.txt" % yr
    f = open(fname, "r")
    data = []
    for l in f:
        date1, value1 = l.split()
        value = float(value1)
        value = int(1.0/value)
        ys, ms, ds = date1.split("/")
        date = 10000 * int(ys) + 100 * int(ms) + int(ds)
        data.append((date, value))
    f.close()
    return data

# read min/max rate for every month
def find_minmax(yr):
    minmax = [ (9999, 0) ] * 12 
    data = read_year(yr)
    for d, v in data:
        # make month 0 .. 11
        month = (d // 100) % 100 - 1  # 인덱스 no는 해당 월의 -1
        minr, maxr = minmax[month] 
        if v < minr:
            minr = v
        if v > maxr: 
            maxr = v
        minmax[month] = minr, maxr
    return minmax

for yr in years:
    print("%4d: " % yr, end =" ")
    minmax = find_minmax(yr)
    for m in range(12):
        print("%4d/%-4d" % minmax[m], end = " ")
    print()
