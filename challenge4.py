import itertools

def isogram(lst):

    total = len(lst)
    alphabet = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", itertools.repeat(0)))
    for word in lst:
        word = word.upper()
        for char in word:
            alphabet[char] += 1

            if alphabet[char] > 1:

                total -= 1
                break
                print (alphabet)



        alphabet = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", itertools.repeat(0)))

    return total

print (isogram(["tests", "bat", "boy", "next", "test", "bricks", "letter"]))
