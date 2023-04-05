import sys
#tax calculation
#rules: 1)Personal allowance £11,850 0 tax rate
#   2) 0 to 34,500 taxed at 20%
#3)34,501 to 150,000 taxed at 40%
#4) over 150,000 taxed at 45%


#calculate the income tax based on rules prior. Pass salary as an arg
#return the tax amount, thus this is a strict mathematical functions, input->output.
def getIncomeTax(salary):

    personal_allowance=salary-11850     #then add this back on

    if(salary>=0 and salary<=34500):
        salary -= (0.2 * salary)
    elif(salary>=34501 and salary<=150000):
        salary -=(0.4 * salary)
    elif(salary>150000):
        salary -=(0.45 * salary)

    salary+=personal_allowance

    return salary

#Main
#________________________________

print("{}".format(getIncomeTax(4000000)))




