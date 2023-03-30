import sys

def calculate_interest(investment,interest_rate):
    if not(interest_rate>=1 and interest_rate<=100):
        print("interest rate must be a number between 1-100(percentage)")
        exit()
    
    years=0
    while(investment<1000):
        result=(interest_rate*(100**-1))*investment
        investment+=result
        years+=1
        
    print("{} years to achieve £{}".format(years,investment))


#main
#investment,interest_rate
calculate_interest(100,10)

