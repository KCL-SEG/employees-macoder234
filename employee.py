"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:

    def __init__(self, description, salary, hours=0, contracts=0, numContracts=1):
        self.description = description
        self.totalPay = 0
        self.calculatePay(salary, hours, contracts, numContracts)
        self.get_pay()

    def get_pay(self):
        return self.totalPay

    def __str__(self):
        return self.description

    def calculatePay(self, salary, hours, contracts, numContracts):
        if hours:
            self.totalPay = salary * hours
        else:
            self.totalPay = salary

        if contracts:
            self.totalPay += contracts * numContracts


# class Contractors(Employee):
#     def __init__(self, name, salary, hours=0): # 0 means they are monthly payed employees
#         super().__init__(name, salary, hours)

#     def calculateHourSalary(self):
#         super().addPay(self.salary * self.hours)

# class Commission(Employee):
#     def __init__(self, name, salary, hours):
#         super().__init__(name, salary, hours)
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee(
    'Billie works on a monthly salary of 4000.  Their total pay is 4000.', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee(
    'Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee(
    'Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.', 3000, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.', 25, 150, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee(
    'Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.', 2000, 0, 1500,)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee(
    'Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.', 30, 120, 600)
