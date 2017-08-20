# Problem Set 3b
# Nikhil Jayswal
#
# Produce a tuple containing all starting points of 
# matches of key string in a target string
# Iterative method has been used

# Uncomment out the test variables and test code at the end to see output

# test variables
# target strings
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
# key strings
key1 = ''
key2 = 'atg'
key3 = 'gaca'
key4 = 'atgca'

# import string methods
# but don't need this if using target.find()
# instead of find(target, key)
from string import *

# iterative function
def subStringMatchExact(target, key):
    assert len(target) > 0, 'Target must have a length greater than zero'
#    find() works for empty keys
#    assert len(key) > 0, 'Key must have a length greater than zero'
    assert len(target) >= len(key), 'Key is bigger than the target'
    
    # tuple to store all starting points of matches of key in target
    startPoints = ()
    # start search from the beginning of the string
    index = 0
    # while index < length of string
    while (index < len(target)):
        # find key in target starting at index = index
        foundAt = target.find(key, index)
        # if key not found, exit loop
        if foundAt == -1:
            break
        else:
            # update tuple and index
            startPoints = startPoints + (foundAt, )
            # for empty keys of length zero
            if (len(key) == 0): index = foundAt + 1
            else:
                index = foundAt + len(key)
    # return answer
    return startPoints

# test code
# print function returns
print 'RESULTS OF ITERATIVE FUNCTION'
print 'Instances of key in target: ', subStringMatchExact(target1, key1)
print 'Instances of key in target: ', subStringMatchExact(target1, key2)
print 'Instances of key in target: ', subStringMatchExact(target1, key3)
print 'Instances of key in target: ', subStringMatchExact(target1, key4)
print 'Instances of key in target: ', subStringMatchExact(target2, key1)
print 'Instances of key in target: ', subStringMatchExact(target2, key2)
print 'Instances of key in target: ', subStringMatchExact(target2, key3)
print 'Instances of key in target: ', subStringMatchExact(target2, key4)
print 'Instances of key in target: ', subStringMatchExact(target1, target1)

