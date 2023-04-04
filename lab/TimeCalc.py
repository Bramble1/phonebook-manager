#create a program with the following features:
#1.Add two times
#2.Find the difference between two times
#3.Convert to hours         3,4,5 enter time string hh:mm:ss (just extract from string, do boundary checks on input
#4.Convert to minutes
#5.Convert Minutes to time
#6.Convert hours to time
#7.Convert Days to time

#Let's make this program into an OOP program.
#split into functions to get a working iterative prototype and then format into OOP style.

import os

time_string1="20:21:40"
time_string2="03:12:45"




#returns a tuple
def extract_time(buffer):
    #hh:mm:ss length=7 bytes, and we know the locations thus can do o(1) operations.
    hours=(int(buffer[0]))*10 + (int(buffer[1]))
    minutes=(int(buffer[3]))*10+ (int(buffer[4]))
    seconds=(int(buffer[6]))*10 + (int(buffer[7]))

    if not ((hours>=0 and hours<24) and (minutes>=0 and minutes<60) and (seconds>=0 and seconds<60)):
        print("incorrect numbers entered for hh:mm:ss")
        exit()

    return (hours,minutes,seconds)


def format_check(buffer):
    if(len(buffer)!=8):
        print("insufficient characters for date (hh:mm:ss)")
        exit()
    if not(buffer[2]==':' and buffer[5]==':'):
        print("incorrect format (hh:mm:ss)")
        exit()
    
    #time=extract_time(buffer) 


def day_to_hours(days):
    result = 24 * days

    print("(in hours) total={}".format(result))

    



#Main

format_check(time_string1)
time = extract_time(time_string1)
print("hours={}".format(time[0]))
print("minutes={}".format(time[1]))
print("seconds={}".format(time[2]))

os.system('clear')
day_to_hours(3.5)

