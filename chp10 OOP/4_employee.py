class Employee: 
    company = "Google"       # class attributes
    salary = 100

#instance attributes as they are both different 
harry = Employee()  # harry and rajni both are instance of class Employee
rajni = Employee()
harry.salary = 300      
rajni.salary = 400

print(harry.company)      # class attributes
print(rajni.company)          # class attributes
Employee.company = "YouTube"  # class attributes
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)