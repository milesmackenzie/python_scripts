f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
csvread = f.read()
data = csvread.split("\n")


def read_csv(string):
    final_lst = []
    f = open(string, "r")
    csvread = f.read()
    data = csvread.split("\n")
    data.remove(data[0])
    string_list = data
    int_fields = []

    for item in string_list:
        int_fields.append(item.split(","))

    for items in int_fields:
        final_lst.append([int(x) for x in items])

    return(final_lst[0:20])
print(read_csv(cdc_list))

cdc_list = "US_births_1994-2003_CDC_NCHS.csv"



def month_births(lst_lst):
    data = read_csv(lst_lst)
    births_per_month = {}

    for item in data:
        if item[1] not in births_per_month:
            births_per_month[item[1]] = item[4]
        else:
            births_per_month[item[1]] += item[4]

    return births_per_month


def dow_births(input_lst):
    data = read_csv(input_lst)
    day_of_week = {}
    for item in data:
        if item[3] not in day_of_week:
            day_of_week[item[3]] = item[4]
        else:
            day_of_week[item[3]] += item[4]

    return day_of_week

def year_births(input_lst):
    data = read_csv(input_lst)
    year = {}
    for item in data:
        if item[0] not in year:
            year[item[0]] = item[4]
        else:
            year[item[0]] += item[4]

    return year

def dom_births(input_lst):
    data = read_csv(input_lst)
    day_of_month = {}
    for item in data:
        if item[2] not in day_of_month:
            day_of_month[item[2]] = item[4]
        else:
            day_of_month[item[2]] += item[4]

    return day_of_month


def calc_counts(lst, column):
        data = read_csv(lst)

        if column == 1:
            return year_births(lst)
        elif column == 2:
            return month_births(lst)
        elif column == 3:
            return dom_births(lst)
        elif column == 4:
            return dow_births(lst)
        else:
            return "Column does not exist"


dictionary = dom_births(cdc_list)


def min_max(dct, mm):
    num = []
    for item in dct:
        num.append(dct[item])
    if mm == "min":
        return min(num)
    if mm == "max":
        return max(num)

def compare(lst, input_value):
