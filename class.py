class Employee:
   "Srinivas"
   #Common base class for all employees
   empCount = 6
   def __init__(self, name, salary):
      name = "Srinivas"
      self.salary = salary
      Employee.empCount += 1
   def displayCount(self):
      print("Total Employee %d" % Employee.empCount)
   def displayEmployee(self):
      print("Name : ", self.name, ", Salary: ", self.salary)
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)