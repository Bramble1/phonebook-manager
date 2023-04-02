import os
import library      #my custom library, library.py needs to be in same directory

ages=[12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

#array iteration stuff
#1.Record the length of the array in a variable for referencing later.
#2.Display each age to stdout on a newline, thus o(n) linear time
#3.Add one year to every age, and redisplay the ages
#4.delete all ages outside of 16-25yr olds (could use the del function)
#5.Display the count of 16-25yr olds
#6.Invoke the sort method of the ages array and print it
#7.What proportion(fraction i guess) of ages fall between 16-25 and display the result



def age_processing_task():
    #1.
    length=len(ages)
    #2.
    for i in range(0,length,1):
            print("{},".format(ages[i])) 
    #3.
    for i in range(0,length,1):
        ages[i]=ages[i]+1
        print("{},".format(ages[i]))
    #4.
    for i in range(0,length,1):
        if not(ages[i]>=16 and ages[i]<=25):
            ages.pop(i)
    for i in range(0,len(ages),1):
        print("{},".format(ages[i]))


#Main code resides here_______________________________________________________________________

age_processing_task()

