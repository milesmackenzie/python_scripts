# my_num = [1, 2, 3, 4, 5, 6, 7]
#
# def summ(n):
#     total = 1
#     for num in n:
#         total = num * total
#     return total
#
# print (summ(my_num))


# def prime(n):
#     lst = []
#     for num in list(range(1, n + 1)):
#         if n % num == 0:
#             lst.append(n)
#     if len(lst) == 2:
#         return True
#     else:
#         return False
#
# print (prime(13))
#
#
# def all_prime(x):
#     numbers = list(range(1, x + 1))
#     lst2 = []
#     for num2 in numbers:
#         if prime(num2) == True:
#             lst2.append(num2)
#     return lst2
#
# print (all_prime(100))

# factorial

# def factorial(n):
#     total = 1
#     for num in list(range(1, n + 1)):
#         total = num * total
#     return total
#
# print (factorial(7))


# number of words
# x = "This is a test string. With commas,"
# def words(n, delimiter = " "):
#     lst = []
#     n = n.replace(",", "")
#     n = n.replace(".", "")
#     n = n.split(delimiter)
#     for x in n:
#         lst.append(len(x))
#
#     return lst
#
# print (words(x))

# def divisible(lst1, num):
#     lst = []
#     for x in lst1:
#         if x % num == 0:
#             lst.append('yes')
#         else:
#             lst.append('no')
#     return lst
#
# print (divisible([10, 25, 20, 31, 33], 5))


# def letter(string, let):
#     lst = []
#     for word in string:
#         print (word[-1])
#         if word[-1] == let:
#             lst.append(word)
#     return lst
#
# print (letter(["I", "am", "in", "loven", "with", "python"], 'n'))

# def letter(string, let):
#     lst = []
#     for idx, word in enumerate(string):
#         if let in word:
#             lst.append(idx)
#     return lst
#
#
# print (letter(["I", "am", "inen", "loven", "with", "python"], 'en'))

income_bounds = [(50000, 0.08), (100000, 0.10), (150000, 0.15)]
# def taxes(tup, inc):
    # print (tup[0])
    # for x in tup:
print (income_bounds[0])

if 4000 < int(income_bounds[0]):
    print (income_bounds[0])

for x in income_bounds:
    print (x[0])
    #     return (min(x[0])
        # if inc > x[0]:
        #     taxes = x[0] * x[1]
        #     inc = inc - x[0]
        # elif inc < x[0]:
        #     taxes = inc * x[1]
            # print (taxes)
            #
            # print (inc)
            # print (taxes)
            # if inc < i[0]:
            #     taxes = inc * i[1]
            # elif inc > i[0]:
            #     taxes = inc * i[0]
            #     inc = inc - i[0]
            #     print (inc)


            # return taxes
