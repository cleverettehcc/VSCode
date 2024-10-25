
#declarations
employeeName = "Jenna Jenkins"
shiftNumber = 15
transactionNumber = 30
transactionDollarValue = 25000
productivityScore = 0
employeeBonus = 0

productivityScore = ((transactionDollarValue / transactionNumber) / shiftNumber)

#if statements
if int(productivityScore) <= 30:
    employeeBonus += 50.00

if int(productivityScore) in range(31, 69):
    employeeBonus += 75.00
    
if int(productivityScore) in range(70, 199):
    employeeBonus += 100.00

if int(productivityScore) >= 200:
    employeeBonus += 200.00
    
#print the outcome
print (f"Employee Name: {employeeName}")
print (f"Employee bonus: ${employeeBonus}")