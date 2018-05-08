import numpy as np

def sum_differences_between_products_and_LCMs(pairs):
    print (pairs)
    sums = []
    lsm = []
    ans = []
    for lst in pairs:
        sums.append(lst[0] * lst[1])

    for x in pairs:
        if x[0] == 0 or x[1] == 0:
                lsm.append(0)
        for i in np.array(range(1, (max(x) * min(x))+1)):
            if i % x[0] == 0 and i % x[1] == 0:
                lsm.append(i)
                break
            else:
                continue
    print (sums)
    print (lsm)
    for idx, item in enumerate(sums):
        ans.append(sums[idx] - lsm[idx])
    return sum(ans)


lst = [[30, 15], [5,9], [12,60], [9,18], [90, 7]]
print (sum_differences_between_products_and_LCMs(lst))
