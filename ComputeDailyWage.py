################################ Compute daily wage

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

print 'Hourly Wage: ', hourlyWage

################################## Compute weekly wage

def computepay ( w,  m , e , g ):
    total = float(wage) - (float(mileage)/float(gas)) - float(expenses)
    return total

#date = raw_input("Enter Beginning and End dates of the week: ")

#input = raw_input("How many days were worked: ")
#days = int(input)

############## Day 1 #######################

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

print 'Day 1 Total: ', computepay ( wage, mileage , expenses , gas )

day1 = computepay ( wage , mileage , expenses , gas )

############## Day 2 ########################

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

print 'Day 2 Total: ', computepay ( wage , mileage , expenses , gas )

day2  = computepay ( wage , mileage , expenses , gas )

weekwage = day1 + day2

print "Your weekly wage for ", date , "is: " , weekwage , "dollars."
