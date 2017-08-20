# Problem Set 3a
# Nikhil Jayswal
#
# Count number of instances of key string in a target string using iterative 
# and recursive methods

# Uncomment out the test variables and test code at the end to see output

# test variables
# target strings
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
# key strings
key1 = 'a'
key2 = 'atg'
key3 = 'gaca'
key4 = 'atgca'

# import string methods
# but don't need this if using target.find()
# instead of find(target, key)
from string import *

# iterative function
def countSubStringMatch(target, key):
    assert len(target) > 0, 'Target must have a length greater than zero'
    assert len(key) > 0, 'Key must have a length greater than zero'
    assert len(target) >= len(key), 'Key is bigger than the target'
    
    # variable to keep track of instances of key in target
    instances = 0
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
            # update instances and index
            instances = instances + 1
            index = foundAt + len(key)
    # return answer
    return instances

# recursive function
def countSubStringMatchRecursive(target, key):
#    these statements can be problematic in recursion
#    assert len(target) > 0, 'Target must have a length greater than zero'
#    assert len(key) > 0, 'Key must have a length greater than zero'
#    assert len(target) >= len(key), 'Key is bigger than the target'
    
    # if there is no instance of key, return zero
    if target.find(key) == -1: return 0
    
    else:
        # find the first instance's position
        foundAt = target.find(key)
        # slice the target function
        indexStart = foundAt + len(key)
        subTarget = target[indexStart:]
        # return 1(for the first instance) + call function with subTarget
        return 1 + countSubStringMatchRecursive(subTarget, key)

# test code
# print function returns
print 'RESULTS OF ITERATIVE FUNCTION'
print 'Instances of key in target: ', countSubStringMatch(target1, key1)
print 'Instances of key in target: ', countSubStringMatch(target1, key2)
print 'Instances of key in target: ', countSubStringMatch(target1, key3)
print 'Instances of key in target: ', countSubStringMatch(target1, key4)
print 'Instances of key in target: ', countSubStringMatch(target2, key1)
print 'Instances of key in target: ', countSubStringMatch(target2, key2)
print 'Instances of key in target: ', countSubStringMatch(target2, key3)
print 'Instances of key in target: ', countSubStringMatch(target2, key4)
print 'Instances of key in target: ', countSubStringMatch(target1, target1)

print 'RESULTS OF RECURSIVE FUNCTION'
print 'Instances of key in target: ', countSubStringMatchRecursive(target1, key1)
print 'Instances of key in target: ', countSubStringMatchRecursive(target1, key2)
print 'Instances of key in target: ', countSubStringMatchRecursive(target1, key3)
print 'Instances of key in target: ', countSubStringMatchRecursive(target1, key4)
print 'Instances of key in target: ', countSubStringMatchRecursive(target2, key1)
print 'Instances of key in target: ', countSubStringMatchRecursive(target2, key2)
print 'Instances of key in target: ', countSubStringMatchRecursive(target2, key3)
print 'Instances of key in target: ', countSubStringMatchRecursive(target2, key4)
print 'Instances of key in target: ', countSubStringMatchRecursive(target1, target1)

# print correct answers
print 'CORRECT ANSWERS'
print 'Instances of key in target: ', target1.count(key1)
print 'Instances of key in target: ', target1.count(key2)
print 'Instances of key in target: ', target1.count(key3)
print 'Instances of key in target: ', target1.count(key4)
print 'Instances of key in target: ', target2.count(key1)
print 'Instances of key in target: ', target2.count(key2)
print 'Instances of key in target: ', target2.count(key3)
print 'Instances of key in target: ', target2.count(key4)
print 'Instances of key in target: ', target1.count(target1)


