def bill(total, tax, tip):
    total_and_tax = total + (total * tax)
    total_all = total_and_tax + (total_and_tax * tip)
    return total_all

print (bill(120, 0.05, 0.25))
