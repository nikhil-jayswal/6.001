# Solves the 0/1 knapsack problem using memoization and decision tree

# Each node of the decision tree has three values: current Index, available weight
# and current value. Based on the decision to take or not to take, the next node is
# constructed. At each node, the solution is the best solution among the children.

# The Memo is a dictionary where the keys are a tuple of current Index and available
# weight and they are matched to solution to the knapsack at that node.
# The Memo is a little different from the decision tree. Do a hand simulation to
# better understand the difference. The Memo stores answers to problems. See the final
# memo to understand.

# Weights is a list of weights of items.
# Values is a list of values of the items.
# Items = Number of items (Might not be necessary)
 
# See test.py in working directory
# Note: Dictionaries are passed by reference
# How to calculate numCalls or How to use global variables.

# counter to track number of calls
numCalls = 0

# function called by user
def knapsack(Weights, Values, AvailableWeight):
    # initialize an empty dictionary of results
    Memo = {}
    # calculate the current Index of decision tree
    Index = len(Weights) - 1
    # call the solver function
    ans = SolveKnapsack(Weights, Values, Index, AvailableWeight, Memo)
    print 'Max Value of items in knapsack is:', ans
    global numCalls
    print 'Number of Calls:', numCalls
    print 'Memo:', Memo
    return None

def SolveKnapsack(Weights, Values, Index, AvailableWeight, Memo):
    # increment number of calls by 1
    global numCalls
    numCalls += 1
    
    # check if already solved
    if (Index, AvailableWeight) in Memo:
        return Memo[(Index, AvailableWeight)]
    
    # else, solve recursively and store results
    else:
        # Base Case - Only one item, Index = 0
        # Take item if weight of item <= Available Weight
        if Index == 0:
            if Weights[Index] <= AvailableWeight:
                Memo[(Index, AvailableWeight)] = Values[Index]
            else:
                Memo[(Index, AvailableWeight)] = 0
            return Memo[(Index, AvailableWeight)]
            
        # general case
        # Do not Take branch
        Without_Index = SolveKnapsack(Weights, Values, Index - 1, AvailableWeight, Memo)
        
        # Take branch - this only exists if item can be taken, i.e
        # if weight of item is not greater than the available weight
        # Hence, if the item cannot be taken, we store the value of the
        # do not take brach as the result
        if Weights[Index] > AvailableWeight:
            Memo[(Index, AvailableWeight)] = Without_Index
            return Memo[(Index, AvailableWeight)]
        else:
            With_Index = Values[Index] + SolveKnapsack(Weights, Values, Index - 1, AvailableWeight - Weights[Index], Memo)
            
        # Answer is branch with the greater value
        ans = max(Without_Index, With_Index)
        # store answer
        Memo[(Index, AvailableWeight)] = ans
        return Memo[(Index, AvailableWeight)]  

# testing code
# Note: test each case separately, else numCalls gets added up
# Weights = [5,3,2]
# Values = [9,7,8]
# MaxWeight = 5
# knapsack(Weights, Values, MaxWeight)

Weights = [1,1,5,5,3,3,4,4]
Values = [15,15,10,10,9,9,5,5]
MaxWeight = 8
knapsack(Weights, Values, MaxWeight)
