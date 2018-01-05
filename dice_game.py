from math import sqrt
import random

def dice(num1, num2):
    lst = []
    lst2 = []
    for num in range(1, num1+1):
        num = random.choice(list(range(1, 7)))
        lst.append(num)



    for num2 in range(1, num2+1):
        num2 = random.choice(list(range(1, 7)))
        lst2.append(num2)



    print ("Player 1 total: " + str(sum(lst)))
    print ("Player 2 total: " + str(sum(lst2)))

    if sum(lst) > sum(lst2):
        return "Player 1 wins"
    else:
        return "Player 2 wins"


print (dice(2, 2))
