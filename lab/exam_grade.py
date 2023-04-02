import sys
import os

#user_input function which does type conversions for us
def user_input(cast_type):
    buffer=None
    if(cast_type=='i'):
        buffer=int(input("Enter: "))
    elif(cast_type=='f'):
        buffer=float(input("Enter: "))
    elif(cast_type=='s'):
        buffer=input("Enter: ")     #string is taken as default for input()
       
    return buffer

#grade boundary function
def grade_boundaries(mark):
    if not (mark>=1 and mark<=100):
        print("Error:mark must be between 1 & 100.\n")
        exit()

    if(mark<50):
        print("Fail\n")
    elif(mark>=50 and mark<=60):
        print("Pass\n")
    elif(mark>=61 and mark<=70):
        print("Merit\n")
    elif(mark>=71 and mark<=100):
        print("Distinction\n")

#Main code resides here
def Main():
    grade_boundaries(user_input('i'))
    exit()


#_______________________________________________________________________
Main()
