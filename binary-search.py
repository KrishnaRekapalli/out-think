"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):

    startPointer = 0
    endPointer = len(input_array)-1
    
   # print startPointer
    #print endPointer
    ite = 0
    while (startPointer != endPointer) :

        ite = ite+1

        midPointer = (startPointer+endPointer)//2
        #print startPointer, endPointer
        #print midPointer
        
        if input_array[midPointer] >= value:
            #print 'left'

            
            #The value is in the left half
            endPointer = midPointer
            
        elif input_array[midPointer] < value:
            #print ' right'

            startPointer = midPointer+1
            #print startPointer
            
    if input_array[startPointer] == value:
        return startPointer
    else:
        return -1
            
        
    """Your code goes here."""
    return -1

test_list = [1,3,9,11,15,19,29, 299, 2222, 3333, 4444, 5555, 6666]
test_val1 = 25
test_val2 = 6666
print binary_search(test_list, test_val2)
print binary_search(test_list, test_val1)
#print binary_search(test_list, test_val2)