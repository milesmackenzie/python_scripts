print ("hello world")



x = int(input('Enter a number: '))
y = 1
z = 0
while y <= x:
    z += y
    y += 1
print(z)

x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

if x > y:
    print ("The first number is larger")
else:
    print ("The second number is larger")

p = int(input('Enter a number: '))

if p < 0:
    print ("Your number is Negative")
elif p > 0:
    print ("Your number is Positive")
else:
    print ("Your number is zero")


x = int(input('Enter a number: '))
z = 0
y = 1
while y <= x:
    z += (x - 1)
    y += 1
print(z)


x = int(input('Enter a number: '))
y = 1
z = 1
while y <= x:
    z *= y
    print(z)
    y += 1
print(z)
