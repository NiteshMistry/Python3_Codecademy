class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)
# prints "<class '__main__.Facade'>"
# In Python __main__ means “this current file that we’re running” and so one could read the output from type() to mean “the class Facade that was defined here, in the script you’re currently running.”