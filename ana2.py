h = ['bat', 'bat', 'rats', 'god', 'dog', 'cat', 'arts', 'star', 'rats']

def find_ana(x):
    sorted_list = []
    ana_list = []
    for i in x:
        print (i)
        sorted_list.append(sorted(i))
        print (sorted_list)
    for r in range(0, len(sorted_list)):
        if sorted_list.count(sorted_list[r]) != 1:
            ana_list.append(x[r])
    return ana_list
print (find_ana(h))
