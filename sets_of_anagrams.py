def set_anagram(t):
    dict = {}
    new_list = []
    total = 0
    for i in t:
        n_list = sorted(i)
        n_list = ''.join(n_list)
        new_list.append(n_list)

    for l in new_list:
        if new_list.count(l) != 1:
            dict[l] = new_list.count(l)
    for o in dict:
        total += 1
    return total

print (set_anagram(["bat", "tab", "rock", "cork", "abt", "it", "ti"]))
