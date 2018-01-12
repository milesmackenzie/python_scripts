x = int(input('Enter a number: '))

nums = list(range(1, x + 1))

number_list = []

for num in nums:
    if x % num == 0:
        number_list.append(num)

if len(number_list) <= 2:
    print ("Your number is prime")
else:
    print ("Your number is not prime")
