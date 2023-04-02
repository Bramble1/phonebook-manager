import sys
import os

#Calculator program for two numbers

def get_input():
    #number=int(input("Enter a number:"))
    number=input("Enter: ")
    return number


#HOW ABOUT keep the same, but if the user enters multiple numbers for exponent, it just
#adds onto the exponent number ,before appling it to result


def addition(values,element_number):
    sum=0
    for i in range(0,element_number,1):
        sum+=values[i]

    return (sum)

def subtraction(values,element_number):
    sum=0
    for i in range(0,element_number,1):
        sum -=values[i]

    return (sum)

def multiplication(values,element_number):
    sum=1
    for i in range(0,element_number,1):
        sum*=values[i]
    
    return(sum)

def division(values,element_number):
    sum=1
    for i in range(0,element_number,1):
        sum*= (values[i]**-1)

    return (sum)

def exponent(base,values,element_number):
    exponent=0
    for i in range(0,element_number,1):
        exponent+=values[i]
    sum = base**exponent
    return (sum)
     

#or just interpret each line the user enters
# thus if they enter a '+' and then followed by a list of numbers, they
#wish to be in the sum, so will need to be a string

def test():
    result=0

    while(1):
        print("\tResult={}\n".format(result))
        print("Now changing result to 100\n")
        result=100



def menu():
    result=0
    while(1):
        os.system('clear')
        print("\tResult={}\n".format(result))
        print("(1) addition\n(2) subtraction\n(3) multiplication\n(4) division\n(5)exponents\n(6)reset result\n")
        option=get_input()
        print("Enter number(enter 'c' to calculate):")
        numbers=[]
        num=0
        while(1):
            num=get_input()
            if(str(num)=="c"):
                break
            numbers.append(int(num))

        if(int(option)==1):
            result+=addition(numbers,len(numbers))
        elif(int(option)==2):
            result+=subtraction(numbers,len(numbers))
        elif(int(option)==3):
            if(result==0):
                result=1
            result*=multiplication(numbers,len(numbers))
        elif(int(option)==4):
            if (result==0):
                result=1
           # result *=division(numbers,len(numbers))
            sum =division(numbers,len(numbers))
            result*=sum
        elif(int(option)==5):
            result = exponent(result,numbers,len(numbers))
        elif(int(option)==6):
            result=0


         

        
    
    

   # if(option==1):
    #    result=addition(numbers,len(numbers))
     #   result=20
        
    #result=5000

#+ need to account for number of operations, in order to actually make
#an actually good calculator
#for example: num1 + num2 + num3 * num6, or just have a menu feature
#and save the result in a variable which is always on display, with the option
#to reset it back to 0 maybe, thus we can get away without doing anything
#complex in regards to string manipulation

#Main
menu()
#test()

    


