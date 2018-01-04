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

def letter(string, let):
    lst = []
    for idx, word in enumerate(string):
        if let in word:
            lst.append(idx)
    return lst


print (letter(["I", "am", "inen", "loven", "with", "python"], 'en'))
