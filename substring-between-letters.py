# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start = word.find(start) + 1
  end = word.find(end)
  if end < 0:
    return word
  return word[start:end]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"