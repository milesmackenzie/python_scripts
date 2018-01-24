

def solve(z):
    lst = list(range(0, 10000))
    lst2 = []
    lst_p = []
    neww_lst = []

    for num in lst:
        prime = True
        for i in range(2, num):
            if (num % i==0):
                prime = False
        if prime:
            lst.remove(num)

    lst = [str(b) for b in lst]

    for nums in lst:
        for n in nums:
            if n == "3" or n == "5" or n == "7" or n == "2":
                lst2.append(nums)
            else:
                pass

    for h in lst2:
        if h in lst:
            lst.remove(h)



    lst = [int(x) for x in lst]

    return lst[z]

print (solve(8))
