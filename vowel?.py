def check_vowel(string, position):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()
    print (string)
    print (position)
    print (string[position])
    if abs(position) > len(string):
        return False
    elif string[position] in vowels:
        return True
    elif string[position] not in vowels:
        return False

print (check_vowel('fpaqkvmqhpbvhriatujlepbkplxtkwftgwdmtyjjucuhqdhcmpsbankzedcihpbsshjepxcemmgktswmiaubeulbgcapltbcguycyycekymmhpmdiilutztppveuwamuypbe', -5))
