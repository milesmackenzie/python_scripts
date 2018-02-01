x = input('Enter a sentence: ')

vowels = ["a", "e", "i", "o", "u"]

for letter in x:
    if letter in vowels:
        x = x.replace(letter, "")

print (x)
