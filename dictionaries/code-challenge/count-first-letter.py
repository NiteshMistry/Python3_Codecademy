# Write your count_first_letter function here:
def count_first_letter(names):
  count = {}
  for key, value in names.items():
    if key[0] not in count:
      count[key[0]] = 0  
    count[key[0]] += len(value)
  return count

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}