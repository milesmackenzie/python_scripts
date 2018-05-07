import string

def alphabetic(s):
    i = 0
    dic = dict(zip(string.ascii_lowercase, range(1,27)))
    s = list(s)
    print (s)
    ss = []
    b = []
    for let in s:
        ss.append(dic[let])
    for num in range(0, len(ss) - 1 ):
        if ss[num] <= ss[num+1]:
            pass
        else:
            return False
    return True


print (alphabetic('door'))
