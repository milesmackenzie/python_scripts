x = int(input('Enter a number: '))

x = range(1, x + 1)
x = list(x)
print (x)

factorial = 1


for i in x:
    factorial = factorial * i
    print (factorial)
