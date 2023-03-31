import sys

#input an integer between two limits, give the user 3 attempts to enter a number
#within the specified boundary



#Function definitions
#_______________________________
def boundary_check(min,max):
    number=-1
    tries=0
    while not(number>=min and number<=max):
        print("Enter a number between {} and {}".format(min,max))
        number=int(input("Enter: "))
        tries+=1

        if(tries==3):
            print("You've used up your three attempts!")
            exit()
        
    print("You entered {}.\n".format(number))


#Main code Where we call our function
#________________________________________
boundary_check(1,100)
