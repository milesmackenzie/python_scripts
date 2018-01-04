plaintext = "regular message letter, mail, mail, locks"

def countLetters(word):
  word = word.replace(" ", "")
  word = word.replace(",", "")
  word = sorted(word)
  # print (word)
  letterdict = {}
  for letter in word:
    letterdict[letter] = 0
  for letter in word:
    letterdict[letter] += 1
  return letterdict


print (countLetters(plaintext))
