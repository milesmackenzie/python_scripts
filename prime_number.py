x = int(input("Enter a number: "))

z = 1

list_number = []


while z < x:
    if x % z == 0:
        list_number.append(z)
    z += 1

if len(list_number) == 1:
    print ("Your number is a prime number")
else:
    print ("Your number is not a prime number")
