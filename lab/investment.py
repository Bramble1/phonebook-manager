import sys


#calculate years for an investment to compound enough specified intereate to reach a target amount


#Function definitions
#____________________________________________________________

def calculate_interest(investment,interest_rate,target_value):
    if not(interest_rate>=1 and interest_rate<=100):
        print("interest rate must be a number between 1-100(percentage)")
        exit()
    
    years=0
    while(investment<target_value):
        result=(interest_rate*(100**-1))*investment
        investment+=result
        years+=1
        
    print("{} years to achieve £{}".format(years,investment))


#Main Where we call our functions
#___________________________________________________________

#investment,interest_rate,target_value (arguments for function, didn't put in variables for performance reasons, However it makes it less readable)
calculate_interest(100,10,1000)

