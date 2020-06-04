def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return  age

my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)

print("I am %d years old and my dad is %d years old" %(my_age,dads_age))