# check out the pseudocode and algorithm first
# do a hand simulation to better understand the code

# function to combine two sorted lists
def CombineLists(array1, array2):

    # counters for the lists
    index1 = 0
    index2 = 0
    
    # lengths of the two lists
    limit1 = len(array1)
    limit2 = len(array2)
    
    # list that is to be returned at the end, initially empty
    Ans = []
    
    # start of loop
    while True:
        
        # compare elements and append smaller element to Ans
        
        # if smaller element belongs to first list, append
        # and update index1
        if array1[index1] < array2[index2]:
            Ans.append(array1[index1])
            index1 = index1 + 1
        
        # if smaller element belongs to second list, append
        # and update index2
        else:
            Ans.append(array2[index2])
            index2 = index2 + 1
       
        # if any counter exceeds list length, append remaining
        # part of longer list to Ans and quit
        if index1 == limit1:
            # appends a list instead of elements
            # Ans.append(array2[index2:])
            # copy and append individual elements instead
            for i in range(index2, limit2):
                Ans.append(array2[i])
            break
        
        elif index2 == limit2:
            # appends a list instead of elements
            # Ans.append(array2[index2:])
            # copy and append individual elements instead
            for i in range(index1, limit1):
                Ans.append(array1[i])
            break
        
    # end of loop
        
    # return combined list
    return Ans           

# testing code for CombineLists
# print CombineLists([1],[2])
# print CombineLists([2],[1])
# print CombineLists([2,3],[1,5])
# print CombineLists([4],[1,3])
# print CombineLists([1,3],[4])
# print CombineLists([1],[3,5])

# recursive function to perform merge sort
def MergeSort(array):
    
    # base case - list of length 2 or 1
    # for list of length 2, combine lists - [list[0]], [list[1]]
    # for list of length 1, return the list
    if len(array) == 1:
        return array
    if len(array) == 2:
        return CombineLists([array[0]], [array[1]])
    
    # else, combine sorted halves
    else:
        mid = len(array) / 2
        array1 = MergeSort(array[:mid])
        array2 = MergeSort(array[mid:])
        return CombineLists(array1, array2)

# testing code for MergeSort
print MergeSort([1,2])
raw_input()
print MergeSort([2,1])
raw_input()
print MergeSort([1,3,2])
raw_input()
print MergeSort([5,4,3,2,1])
raw_input()
print MergeSort([1,2,3,4,5])
