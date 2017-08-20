# Problem Set 2a
# Nikhil Jayswal
#
# Find the largest number of McNuggets that cannot
# be bought in exact quantity
#

Nuggets = 1
solution = None

# solves using exhaustive enumeration
def solve(NumberNuggets):
    """Checks if there is a possible solution to the Diophantine
    equation 6a + 9b +20c = n"""
    CountSix = 0
    CountNine = 0
    CountTwenty = 0

    MaxSix = (NumberNuggets / 6) + 1
    MaxNine = ((NumberNuggets - 6 * CountSix) / 9) + 1
    MaxTwenty = ((NumberNuggets - 6 * CountSix - 9 * CountNine) / 20) + 1

    flag = 0
    for CountSix in range(0, MaxSix):
        for CountNine in range (0, MaxNine):
            for CountTwenty in range (0, MaxTwenty):
                Total = 6 * CountSix + 9 * CountNine + 20 * CountTwenty
                if Total == NumberNuggets:
                    flag = 1
                    return True
    return False

while (True):
#    print Nuggets
    
    if solve(Nuggets) == False: #if no solution, then save value
#        print solution
        solution = Nuggets
    
    else: #if solution found, check solutions for Nuggets+1,...,Nuggets+5
        flag = 0
        
        for var in range(Nuggets+1, Nuggets+6): #for Nuggets+1,...,Nuggets+5
            if solve(var) == False: #if no solution, save value and stop checking
                flag = 1
                solution = var
                break
        
        if flag == 0: #if solutions found for all values, stop loop
            print 'Largest number of McNuggets that cannot be bought in exact quantity: ', solution #print last saved value
            break           
    
    Nuggets = solution + 1 #update Nuggets
