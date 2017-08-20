# check out the pseudocode and algorithm first

def BubbleSort(array):
    
    # get length of list
    limit = len(array)

    # start of outer loop        
    for i in range(0, limit):
      
        # track number of swaps
        numSwaps = 0
        
        # "bubble" up the largest element in the list to the end
        # start of inner loop
        for j in range(0, limit - i - 1):  
               
            if array[j] > array[j + 1]: 
                # swap
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
                # increase swap counter
                numSwaps = numSwaps + 1
                
        # end of inner loop
        
        # if no swaps occurred, list is sorted
        # stop
        if numSwaps == 0:
            break
    
        # for debugging/understanding
        print 'List at the end of iteration', i + 1
        print array
    
    # end of outer loop        
    
    # return sorted list
    print 'Sorted List is'
    return array

# testing code
print BubbleSort([1,3,5,2])
print BubbleSort([1,2,3,4,5])
print BubbleSort([2,6,3])
print BubbleSort([6,5,4,3,2,1])
