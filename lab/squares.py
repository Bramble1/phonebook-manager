import sys

#Program to use a while loop to iterate through the number line, and print the number
#and their associated square, s(x) = x^2 . Association mapping in mathematics.

#Main code resides in this function
def square():
    i=1
    while(i>=1 and i<=100):
        result=i**2
        if(result>2000):
            break
        
        print("{}->{}".format(i,result))
        i+=1


#calling our function
square()



