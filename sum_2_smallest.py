s = [343445353, 35, 3453545353453, 10, 1, 2, 4, 5, 6, 7]

def sum_two_smallest_numbers(numbers):
  numbers_list = []
  for number in numbers:
    if number == min(numbers):
      numbers_list.append(number)
      numbers.remove(number)
      print (numbers)
      print (numbers_list)
      for number in numbers:
        if number == min(numbers):
          numbers_list.append(number)
          print (numbers_list)
          return sum(numbers_list)


print (sum_two_smallest_numbers(s))
