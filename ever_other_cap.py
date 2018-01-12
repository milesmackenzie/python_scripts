x = input('Enter a sentence: ')

x = list(x)


for i, letter in enumerate(x):
    if i % 2 == 0:
        x[i] = letter.upper()
    else:
        x[i] = letter.lower()

x = ''.join(x)

print (x)
