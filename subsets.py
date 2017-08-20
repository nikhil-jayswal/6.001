def binary(number, digits):
    """Returns binary representation of number
       digits - number of digits in the binary number required"""    
    # initialize an empty list
    ans = []
    # make list of size N to hold N digits
    for i in range(0, digits):
        ans.append(0)
    
    # generate binary representation
    res = number
    index = 0
    while res > 0:
        ans[index] = res % 2
        res = res / 2
        index = index + 1
    return ans

# list of N objects
Array = [1,2,3,4,5]
N = len(Array)
for i in range(0, 2**N):
    # get the binary form of i
    # each binary number has to be N digits long
    # representing N objects
    num = binary(i, N)  
    subset = []
    for j in range(0, N):
        if num[j] == 1:
            subset.append(Array[j])
    print 'Subset #', i + 1, ':',subset
