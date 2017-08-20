# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name: Nikhil Jayswal
#
# Given the amount of work a student wants to do, the program returns a list of
# subjects that maximizes the amount of value.

# The goal of this problem set is to implement a dynamic programming algorithm 
# and learn how to pass functions as arguments.


import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # open file
    inputFile = open(filename)
    
    # initialize an empty dictionary
    subjects = {}
    
    # Parse the name, value, and work of each subject and create a dictionary 
    # mapping the name to the (value, work).
    for line in inputFile:
        # strip line of line break character
        line = line.strip()
        # split line to get subject name, value and work
        data = line.split(',')
        # subject name
        name = data[0]
        # subject value
        value = int(data[1])
        # subject work
        work = int(data[2])
        # add entry in dictionary
        subjects[name] = (value, work)
    
    return subjects

    # end of function 

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        # since subject names are mapped to a tuple, they can be accessed
        # using index 0 and 1 too. I don't know why this works. Got it! They
        # are aliases for 0,1. Look at the lines at the beginning of the file. 
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # Note that the subject dictionary is sorted by subject names prior
    # to printing.

    # initialize empty output dictionary
    answer = {}
    # select the best subject and add the subject details to output dictionary
    # keep track of total work
    totalWork = 0
    while True:
        # select best subject according to value, work or the ratio value/work
        # initial assumption for best subject
        best = (0,maxWork)
        bestSub = ''
        for subject in subjects:
            # if a better subject is found, replace the best subject
            # subject cannot be repeated
            if subject not in answer and comparator(subjects[subject],best) == True:
                bestSub = subject
                best = subjects[subject]
        
        # check total work hours, quit if exceeded
        totalWork = totalWork + best[WORK]
        if totalWork <= maxWork:
            # add subject details to dictionary
            answer[bestSub] = best
        else:
            break
    
    # return answer
    return answer
        
    
def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    start_time = time.time()
    subjects = loadSubjects(SUBJECT_FILENAME)
    maxWork = 8
    answer = bruteForceAdvisor(subjects, maxWork)
    end_time = time.time()
    printSubjects(answer)
    print 'Time taken: ', end_time - start_time
    return None
    
# Problem 3 Testing and Observations
# ==================================
#
bruteForceTime()
# Observation: 
# For maxWork = 2, time taken is 0.006
# For maxWork = 5, time taken is 0.2
# For maxWork = 8, time taken is 4.8
# For maxWork = 10, time taken is 34.44

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # initialize an empty Memo of solutions and dictionary Keep of included
    # subjects
    Memo = {}
    Keep = {}
       
    # get list of subjects
    names = subjects.keys()
    
    # starting index for decision tree
    index = len(names) - 1
    
    # solve using dynamic programming
    ans = dpSolve(subjects, index, maxWork, Memo, Keep)
    
    # create dictionary of subjects
    limit = maxWork
    outputSubjects = {}
    i = len(names) - 1
    while i >= 0:
        # if subject is to be included, copy details
        if Keep[(i,limit)] == 1:
            outputSubjects[names[i]] = subjects[names[i]]
            limit = limit - subjects[names[i]][WORK]
        i = i - 1
     
    # return subjects
    return outputSubjects
     
def dpSolve(subjects, index, availableWork, Memo, Keep):
    # get subject details - value and work hours
    details = subjects.values()
    
    # see knapsack solution code to understand
    if (index, availableWork) in Memo:
        return Memo[(index, availableWork)]
    else:
        if index == 0:
            if details[index][WORK] <= availableWork:
                Memo[(index, availableWork)] = details[index][VALUE]
                Keep[(index, availableWork)] = 1
            else:
                Memo[(index, availableWork)] = 0
                Keep[(index, availableWork)] = 0
            return Memo[(index, availableWork)]
        without_index = dpSolve(subjects, index - 1, availableWork, Memo, Keep)
        if details[index][WORK] > availableWork:
            Memo[(index, availableWork)] = without_index
            Keep[(index, availableWork)] = 0
            return Memo[(index, availableWork)]
        else:
            with_index = details[index][VALUE] + dpSolve(subjects, index - 1, availableWork - details[index][WORK], Memo, Keep)
        ans = max(without_index, with_index)
        if ans == without_index:
            Keep[(index, availableWork)] = 0    
        else:
            Keep[(index, availableWork)] = 1
        Memo[(index, availableWork)] = ans
        return Memo[(index, availableWork)]  
#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    start_time = time.time()
    subjects = loadSubjects(SUBJECT_FILENAME)
    maxWork = 50
    answer = dpAdvisor(subjects, maxWork)
    end_time = time.time()
    printSubjects(answer)
    print 'Time taken: ', end_time - start_time
    return None

# Problem 5 Testing and Observations
# ==================================
#
dpTime()
# Observation: 
# For maxWork = 8, time taken is 0.01
# For maxWork = 30, time taken is 0.054
# For maxWork = 50, time taken is 0.074 
