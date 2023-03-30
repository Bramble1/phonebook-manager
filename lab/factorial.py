import sys

def get_input():
    number=int(input("Enter a number:"))
    return number



#Factorial algorithm using while loop
def factorialV1(number):
    i=number-1
    print("!{}=".format(number))
    while(i>0):
        number*=i
        i-=1
    print(number)
        

#Factorial algorithm using recursion
def factorialV2(number):
    if(number==0):
        return 1
    else:
        return (number*factorialV2(number-1))

#Factorial algorithm using for loop
def factorialV3(number):
    print("!{}=".format(number))
    for i in range(number-1,0,-1):
        number*=i
    
    print(number)


#main code
#_________________________________________________

print("Factorial Algorithm using While loop:\n")
print("_____________________________________\n")
factorialV1(get_input())


print("\nFactorial Algorithm using recursion:\n")
print("____________________________________\n")
print("{}".format(factorialV2(get_input())))


print("\nFactorial Algorithm using for loop:\n")
print("___________________________________\n")
factorialV3(get_input())
