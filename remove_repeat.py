n = [1, 2, 3, 4, 5, 5]

def remove_first(n):
    n_list = []
    for x in n:
        if n.count(x) != 1:
            n.remove(x)
            return n


remove_list = remove_first(n)

print remove_list
