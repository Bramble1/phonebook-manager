import sys

#count vowels in a string vowels = {a,e,i,o,u,y}


#linear o(n)
def count_vowels(buffer):
    counter=0
    buffer.lower()
    for i in range(0,len(buffer),1):
        if(buffer[i].lower()=='a' or buffer[i].lower()=='e' or buffer[i].lower()=='i' or buffer[i].lower()=='o' or buffer[i].lower()=='u' or buffer[i].lower()=='y'):
            counter+=1
    
    print("number of vowels={}".format(counter))


#Main
string="IaUlOo\0"
count_vowels(string)

