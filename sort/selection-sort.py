# check out the pseudocode and algorithm first

def SelSort(array):
    
    # get length of list
    limit = len(array)

    # start of outer loop        
    for i in range(0, limit):
      
        # assume the first element of list to be the smallest
        minVal = array[i] # value of smallest element
        minIndex = i      # position of smallest element
        
        # find the smallest element of the list
        # start of inner loop
        for j in range(i, limit):  
               
            if array[j] < minVal: 
                minVal = array[j]
                minIndex = j
        
        # end of inner loop
        
        # if minIndex has changed, swap elements
        if minIndex != i:
            tmp = array[i]
            array[i] = minVal
            array[minIndex] = tmp
    
        # for debugging/understanding
        print 'List at the end of iteration', i + 1
        print array
    
    # end of outer loop        
    
    # return sorted list
    print 'Sorted List is'
    return array

# testing code
print SelSort([1,3,5,2])
print SelSort([1,2,3,4,5])
print SelSort([2,6,3])
print SelSort([6,5,4,3,2,1])
