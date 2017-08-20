def base_N(number, digits, N):
    """Returns base N representation of number
    digits - number of digits in the number required"""
    # initialize an empty list
    ans = []
    # make list of size N to hold N digits
    for i in range(0, digits):
        ans.append(0)

    # generate base N representation
    res = number
    index = 0
    while res > 0:
        ans[index] = res % N
        res = res / N
        index = index + 1
    return ans

# list of N objects
Array = [1,2,3,4,5]
length = 1
N = len(Array)
for i in range(0, N**length):
    # get the base N representation of i
    # 'length' digits long
    num = base_N(i, length, N)  
    permutation = []
    for j in range(0, length):
        permutation.append(Array[num[j]])
    print 'Permutation #', i + 1, ':',permutation
