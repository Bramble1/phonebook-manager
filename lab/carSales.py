import sys
import csv

#read the .csv file and place them into lists of integers and then perform the following
#calculations being sum of cars sold in each month and Total yearly sales by each manufacturer
#read into two arrays being companies[] and sales[]


#read the file if line equls Ford motor ocmpany, then we
#get the next line, store in a string, and then convert and map
#into a list of integers 
def read_file(filename):
    with open(filename) as f:
        contents = f.readlines()
    f.close()
    
    return contents


def populate_lists(contents):
    
    companies = {
            contents[0]:contents[1],
            contents[2]:contents[3],
            contents[4]:contents[5],
            contents[6]:contents[7],
            contents[8]:contents[9]

            }

    return companies


def calculate_sales(companies):
    for key,value in companies.items():
        print("{} sales monthly:\n\t{}".format(key,value))
        line=value.strip().split(',')
        total=sum(list(map(int,line)))
        print("total={}\n".format(total))
        


#Main
#___________________________________-
contents = read_file("carSale.csv")

companies = populate_lists(contents)


calculate_sales(companies)


#
