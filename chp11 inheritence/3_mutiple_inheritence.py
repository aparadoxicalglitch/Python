class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Employee:
    company = "Visa"
    eCode = 120


class Programmer(Freelancer, Employee):  #  the class we write first in the bracket will have more priority
    name = "Rohit"

p = Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company)