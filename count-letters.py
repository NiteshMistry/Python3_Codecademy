letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  return len(set(word))
  
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4