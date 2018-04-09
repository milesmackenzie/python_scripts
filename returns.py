def returns(holdings, percent, days):
    total = holdings
    percent = percent + 1
    count = 0
    while count < days:
        total = (total * percent)
        count += 1

    return total - holdings

print (returns(10000, 0.0033, 365))
