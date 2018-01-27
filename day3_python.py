# DAY 3 Part 1 practice w/ tuples:

num = input("Enter numbers separated by commas: ")

lst = []
num = num.replace(",", "")
num = num.replace(" ", "")

for x in num:
    lst.append(x)

lst(zipped)
print(lst)

# DAY 3 Part 2 practice w/ dictionaries:

num = input("Enter numbers separated by dashes: ")

my_dct = {}
lst = []

num = num.replace("-", "")
num = num.replace(" ", "")

for x in num:
    lst.append(int(x))

for number in lst:
    my_dct[number] = number * number

print(lst)
print(my_dct)
#
# question 2:

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                       'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                       'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

x = input("Enter a state: ")


if x in state_dictionary:
    print(state_dictionary.get(x))
else:
    print("Capital unknown")

# Question 3:


x = input("Enter coordinates and word: ")

x = x.split(",")

lst = []
my_dct = {}

lst.append(int(x[0]))
lst.append(int(x[1]))

lst = tuple(lst)

my_dct[lst] = x[2]

print(my_dct)

# PART 3 practice w/ sets:

x = input("Enter set of numbers: ")
y = input("Enter another set of numbers: ")

lst = []

x = x.replace(",", "")
x = x.replace(" ", "")
x = list(x)

y = y.replace(",", "")
y = y.replace(" ", "")
y = list(y)

for num in x:
    if num in y:
        lst.append(num)


print(x)
print(y)
print(lst)
# 
# Question 2:

x = input("Enter a list of words: ")

x = x.split()
lst = []
for word in x:
    if x.count(word) == 1:
        lst.append(word)

print(x)
print(lst)
