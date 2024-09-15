# input statements
salary = float(input("Enter salary "))
numDependents = float(input("input number of dependant: "))

# calculate taxes here
stateTax = salary * (6.5 / 100)
print("State tax: $" + str(stateTax))
federalTax =salary * (28 / 100)
print("Federal Tax: $" + str(federalTax))
dependantDeduction = (salary * (2.5 / 100)) * numDependents
print("Dependants: $" + str(dependantDeduction))
totalWithholding = (stateTax + federalTax + dependantDeduction)
takeHomePay = (salary - totalWithholding)

# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))