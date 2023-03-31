import sys
import os

#Function definitions
#_____________________________________________________________

#calculate the average of three exam marks
def boundary_check(average):
    if (average>=65):
        print("Pass! average={}".format(average))
    elif(average<65):
        print("Failed! average={}".format(average))
        

#loop until they enter the correct marks between the boundaries
#enter exam_names as a tuple
def calculate_average(exam_names):
    correct=False
    average=0
    while(correct==False):
        os.system('clear')
        for i in range(0,3,1):
            print("Enter {}".format(exam_names[i]))
            number=int(input("Enter(0-100): "))
            if not(number>=0 and number<=100):
                correct=False
                break       #saves on performance if we find out one is invalid
            else:
                correct=True
                average+=number
                #compounding function for working out the average on the fly

    average = average * (3**-1)

    boundary_check(average) #compounding functions i.e calling a function within a function

#Main Where we call our function
calculate_average(("Maths","English","ICT"))
