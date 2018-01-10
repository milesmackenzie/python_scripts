n = "This is a test, long word"

def is_kiss(words):
    lst = []
    long = []
    words = words.split()
    print (words)
    for i in words:
        if len(i) <= len(words):
            lst.append(i)
        else:
            long.append(i)

    if len(long) >= 1:
        return "Keep It Simple Stupid"
    else:
        return "Good work Joe!"

print is_kiss(n)
    

          # Have Fun!
