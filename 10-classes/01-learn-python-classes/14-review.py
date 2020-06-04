class Student:
  def __init__(self, name, year, day):
    self.name = name
    self.year = year
    self.day = day
    self.grades = []
    self.attendance ={'Monday':True, 
                      'Tuesday':True, 
                      'Wednesday':False,
                      'Thursday':False,
                      'Friday':False}
  
  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)
    
  def get_average(self):
    sum_grades = 0
    for student in self.grades:
      sum_grades += student.score
      return sum_grades/len(self.grades)
  
  def availability(self):
    for key, val in self.attendance.items():
      if key == self.day:
        return val
    
  def __repr__(self):
    return f'Name: {self.name}\nYear: {self.year}\nGrade: {self.get_average()}\nAttendance: {self.availability()}'
 
class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
  def is_passing(self):
    return self.score > Grade.minimum_passing


pieter = Student('Pieter Bruegel the Elder', 8, 'Monday')

pieter_grade1 = Grade(100)
pieter_grade2 = Grade(80)
pieter_grade3 = Grade(60)

pieter.add_grade(pieter_grade1)
pieter.add_grade(pieter_grade2)
pieter.add_grade(pieter_grade3)

print("Grade1: ",pieter_grade1.is_passing())
print("Grade2: ",pieter_grade2.is_passing())
print("Grade3: ",pieter_grade3.is_passing())

print("Avg: ",pieter.get_average())
print("Availability: ",pieter.availability())

print(pieter)