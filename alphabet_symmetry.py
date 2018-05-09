import string
def solve(arr):
    lst = []
    lst2 = []
    total = []
    dic = dict(zip(string.ascii_lowercase, range(1,27)))
    for x in arr:
        lst.append(list(x.lower()))
    for lt in lst:
        for idx, let in enumerate(lt):
            if dic[let] == (idx+1):
                lst2.append(dic[let])
        total.append(len(lst2))
        lst2 = []
    return total
    print (total)
    print (lst2)
    print (lst)
x = ['abode', 'ABc', 'xyzD']
print (solve(x))
