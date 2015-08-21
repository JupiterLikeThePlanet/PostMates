#Compute daily wage

def computepay ( w , m , e , g ):
    total = float(wage) - (float(mileage)/float(gas)) - float(expenses)
    return total

try:
    input = raw_input('Enter Wages: ')
    wage = float(input)
    input = raw_input('Enter Miles: ')
    mileage = float(input)
    input = raw_input('Enter Expenses: ')
    expenses = float(input)
    input = raw_input('Enter Price of Gas: ')
    gas = float(input)

except:
    print "Not a number!"
    quit()

print 'Total: ', computepay ( wage , mileage , expenses , gas )

hours = raw_input('Enter Hours: ')
hourlyWage = computepay ( wage , mileage , expenses , gas ) / float(hours)

<<<<<<< HEAD
print 'Hourly Wage: ', hourlyWage
=======
print 'Hourly Wage: ', hourlyWage

