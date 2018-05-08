def black_or_white_key(key_press_count):
    white = [1,3,4,6,8,9,11,13,15,16,18,20,21,23,25,
    27,28,30,32,33,35,37,39,40,42,44,45,47,49,51,
    52,54,56,57,59,61,63,64,66,68,69,71,73,75,76,
    78,80,81,83,85,87,88]

    if key_press_count in white:
        return "white"
    elif (key_press_count % 88) in white:
        return "white"
    elif (key_press_count % 88) == 0:
        return "white"
    else:
        return "black"

print (black_or_white_key(900))
print (black_or_white_key(43))
print (black_or_white_key(8765))
