import random


my_alphabet = list("abcdefghijklmnopqrstuvwxyz,';.?")
for i in range(3):
    random.shuffle(my_alphabet)
    dst = ''.join(my_alphabet)
    print(dst)
