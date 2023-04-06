#Create assertions whether this function works with a list of integers and strings
#work with the given function.


#count how many times item is found in sequence.
def count(sequence,item):
    sum=0

    for n in sequence:
        if n==item:
            sum+=1
    return sum



#Main program

def test_answer():
    assert count((1,2,3,2),2)==2
    assert count(("1,2,3,2"),"2")==2

