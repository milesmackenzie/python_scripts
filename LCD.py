x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

z = 1
w = 1
list_x = []
list_y = []

while z < x:
    if x % z == 0:
        list_x.append(z)
    z += 1
while w < y:
    if y % w == 0:
        list_y.append(w)
    w += 1

print (list_x)
print (list_y)

min_x = max(list_x)
min_y = max(list_y)

if min_x > min_y:
    for number in list_y:
        if number in list_x:
            print ("The LCD is " + str(number))
            break


else:
    for number in list_x:
        if number in list_y:
            print ("The LCD is " + str(number))
            break
