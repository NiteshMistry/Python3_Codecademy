# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  # word_length = {}
  # for word in words:
  #   if word.isalpha(): word_length[word] = len(word)
  #   else: word_length[word] = 0
  # return word_length
  return {word:(len(word) if word.isalpha() else 0) for word in words}

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}