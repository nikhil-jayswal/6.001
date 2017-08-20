# Problem Set 2b
# Nikhil Jayswal
#
# Find the largest number of McNuggets that cannot
# be bought in exact quantity for a given set of packages
#
bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,20)   # variable that contains package sizes

# solves using exhaustive enumeration
def solve(NumberNuggets, packages):
    """Checks if there is a possible solution to the Diophantine
    equation Xa + Yb +Zc = n; X, Y, Z are package sizes"""
    X = packages[0]
    Y = packages[1]
    Z = packages[2]
    
    CountX= 0
    CountY = 0
    CountZ = 0

    MaxX = (NumberNuggets / X) + 1
    MaxY = ((NumberNuggets - X * CountX) / Y) + 1
    MaxZ = ((NumberNuggets - X * CountX - Y * CountY) / Z) + 1

    flag = 0
    for CountX in range(0, MaxX):
        for CountY in range (0, MaxY):
            for CountZ in range (0, MaxZ):
                Total = X * CountX + Y * CountY + Z * CountZ
                if Total == NumberNuggets:
                    flag = 1
                    return True
    return False
#
# main code
n = 1 # n = Number of McNuggets
while (n < 150): # only search for solutions up to size 150
    if solve(n, packages) == False: #if no solution, then save value
#        print solution
        bestSoFar = n
    
    else: #if solution found, check solutions for n+1,...,n+5
        flag = 0
        
        for var in range(n+1, n+6): #for n+1,...,n+5
            if solve(var, packages) == False: #if no solution, save value and stop checking
                flag = 1
                bestSoFar = var
                break
        
        if flag == 0: #if solutions found for all values, stop loop
            print 'Given package sizes', packages, 'the largest number of McNuggets that cannot be bought in exact quantity is: ', bestSoFar #print last saved value
            break           
    
    n = bestSoFar + 1 #update n

    
