# Problem Set 3c
# Nikhil Jayswal
#
# Match pairs to find near matches of key in target
# See pset spec for clarifications 
# 
# Iterative method has been used

# Uncomment out the test variables and test code at the end to see output

# test variables
# target strings
target1 = 'atgacatgca'
target2 = 'atgaatgcatggatgtaaatgcag'
# key strings
# keys of length 1 are not so good for this problem, beacuse we need two parts 
# after substitution of one element with an empty character
key1 = 'at'
key2 = 'atg'
key3 = 'atgc'
key4 = 'atgca'

# import string methods
# but don't need this if using target.find()
# instead of find(target, key)
from string import *

def subStringMatchExact(target, key):
    assert len(target) > 0, 'Target must have a length greater than zero'
#    for this problem, keys can be empty
#    assert len(key) > 0, 'Key must have a length greater than zero'
#    assert len(target) >= len(key), 'Key is bigger than the target'
    
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
            # for empty keys
            if len(key) == 0: index = foundAt + 1
            else:
                index = foundAt + len(key)
    # return answer
    return startPoints

# iterative function
def constrainedMatchPair(firstMatch, secondMatch, length):
    # variable to store indexes in firstMatch that are to be returned
    pairs = ()
    # for all values in firstMatch
    for firstIndex in firstMatch:
        # check for all values in secondMatch
        for secondIndex in secondMatch:
            # if the indexes are a match, add to answer
            if firstIndex + length + 1 == secondIndex:
                pairs = pairs + (firstIndex, )
                break
    return pairs
    
# tests the function constrainedMatchPair()
def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    print 'target is:', target
    print 'key is:', key
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print '\nbreaking key:', key, 'into', key1, 'and', key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print '\npossible matches for',key1,key2,'start at',filtered

    print '\nReturning matchpoints(can be redundant)'
    return allAnswers

# test code
# print function returns
print 'RESULTS'
print subStringMatchOneSub(key1, target1)
#print subStringMatchOneSub(key2, target1)
#print subStringMatchOneSub(key3, target1)
#print subStringMatchOneSub(key4, target1)
#print subStringMatchOneSub(key1, target2)
#print subStringMatchOneSub(key2, target2)
#print subStringMatchOneSub(key3, target2)
#print subStringMatchOneSub(key4, target2)
#print subStringMatchOneSub(target1, target1)
        
