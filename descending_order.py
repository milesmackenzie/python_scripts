def Descending_Order(num):
    s = str(num)
    s = list(s)
    s = sorted(s)
    s = s[::-1]
    s = ''.join(s)
    return int(s)

s = 46738847
print Descending_Order(s)
