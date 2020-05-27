# Write your max_key function here:
def max_key(my_dictionary):
  max_key = 0
  max_value = 0
  for key, value in my_dictionary.items():
    if value > max_value: max_key, max_value = key, value
  return max_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"