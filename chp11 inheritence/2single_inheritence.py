class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    # company = "Youtube"

    def getLanguage(self):
        
        print(f"The language is {self.language}")
    
        '''  def showDetails(self):
             print("This is an programmer") ''' # if this function will run then p.showDetails() will print this is programmer


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails() # it wil print the same as 'e' because there is nothing in the class programmer
print(p.company) 