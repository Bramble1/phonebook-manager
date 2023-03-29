import sys

#function for obtaining user input and sanatizing and checking
def get_input():
    length=input("Enter Length:")
    width=input("Enter Width:")
    
    #check to make sure length and width are numbers and not ascii
    if(length.isnumeric()==False or width.isnumeric()==False):
        print("Invalid, Must enter only numbers")
        exit()

    return length,width

#if 0, then we do area, if 1 then perimister
def area(width,length):
    result=width*length
    print("area = {}".format(result))



def perimeter(width,length):
    result=(width*2)+(length*2)
    print("perimeter={}".format(result))





inputs = get_input()
result = area(int(inputs[0]),int(inputs[1]))
perimeter(int(inputs[0]),int(inputs[1]))
#result = area(inputs[0],inputs[1])



#function for the calculation of the area and a seperate function for perminter
