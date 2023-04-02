import sys
import os
import math
import library

#print(library.user_input('i',"Enter an integer"))

#pythag = c^2 = a^2 + b^2 , where c is hypotenuse and a and b are the "legs"
#1.find the length of A given B and C
#2.find the length of B given A and C
#3.find the length of C given A and B
#this should be a menu thus requires user interaction

#floats required
def pythag(a,b,c):
    result=0
    if(a==None):
        result=(c**2)-(b**2)
    elif(b==None):
        result=(c**2)-(a**2)
    elif(c==None):
        result=(a**2)+(b**2)
   
   #need to squarroot the result before returning
    return (math.sqrt(result))

def menu():
    os.system('clear')
    print("\t\tPythagoras calculator\n")
    print("1.Find the length of A given B and C.\n")
    print("2.Find the length of B given A and C.\n")
    print("3.Find the length of C given A and B.\n")
    
    return(library.user_input('i',"Option"))

def interpret(option):
    #option=library.user_input('i',"Option:")
    result=0
    if(option==1):
        result=pythag(None,library.user_input('f',"Enter length B"),library.user_input('f',"Enter length C"))
    elif(option==2):
        result=pythag(library.user_input('f',"Enter length A"),None,library.user_input('f',"Enter length C"))
    elif(option==3):
        result=pythag(library.user_input('f',"Enter length A"),library.user_input('f',"Enter length B"),None)
    
    return result


def main():
    print("Unknown length={}".format(interpret(menu())))
    exit()
   
#_________________________________________________________________--
main()


