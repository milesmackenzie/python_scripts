scramble_alph = "ILQEAKFXWCDBNMYZOPJSHGRVUT"


alphabet = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",scramble_alph))
cipher_alphabet2 = dict(zip(scramble_alph,"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

plaintext = "this is a test"

def cipher(text, option='encipher'):
    lst = []
    lst2 = []
    lst3 = []
    text = text.upper()
    print (text)
    if option == "encipher":
        for letter in text:
            if letter == " " or letter == "," or letter == ".":
                letter = str(letter)
                lst.append(letter)
            else:
                letter = alphabet[letter]
                letter = str(letter)
                lst.append(letter)
        lst = "".join(lst)


        for let in text:
            if letter == " " or letter == "," or letter == ".":
                letter = str(letter)
                lst2.append(letter)
        return lst

    else:
        for letter in text:
            if letter == " " or letter == "," or letter == ".":
                letter = str(letter)
                lst3.append(letter)
            else:
                letter = cipher_alphabet2[letter]
                letter = str(letter)
                lst3.append(letter)
        lst3 = "".join(lst3)

        return lst3


print (cipher(plaintext))
