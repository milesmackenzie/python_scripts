def all_perms(x):
    if len(x) <=1:
        return x
    else:
        tmp = []
        for perm in all_perms(x[1:]):
            for i in range(len(x)):
                tmp.append(perm[:i] + x[0:1] + perm[i:])
        return tmp

def total_ana(x):
    total = 0
    list_ana = all_perms(x)
    for i in list_ana:
        total += 1
    return total
print total_ana("123")


print all_perms("123")
