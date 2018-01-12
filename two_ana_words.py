def is_anagram(test, original):
  sorted_test = []
  sorted_original = []
  test = test.upper()
  original = original.upper()
  for i in test:
    sorted_test2 = sorted(i)
    sorted_test2 = ",".join(sorted_test2)
    sorted_test.append(sorted_test2)
  print sorted_test
  for o in original:
    sorted_ori2 = sorted(o)
    sorted_ori2 = ",".join(sorted_ori2)
    sorted_original.append(sorted_ori2)
  if sorted(sorted_test) == sorted(sorted_original):
      return "Words %s and %s are Anagrams" % (test, original)
  else:
      return "Words %s and %s are not Anagrams" % (test, original)


print is_anagram("this", "siht")
