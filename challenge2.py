def remove_item(list_it, it_remove):
    for x in list_it:
        if x == it_remove:
            list_it.remove(x)

            return list_it



n = [1, 2, 3, 4, 5, 4, 4, 3, 4, 3]

print (remove_item(n, 3))
