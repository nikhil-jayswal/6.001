# Problem Set 1a
# Nikhil Jayswal
#
# Finding the 1000th prime
#
# 2 is the first and only even prime; all others are odd
start = 3 #don't need this, can do candidate = 3
count = 1 #counts number of primes found, already have 2 as first prime
candidate = start

while (count < 1000):
    divisor = 2 
    flag = 0   
    while (divisor < candidate):
        if (candidate % divisor == 0): #if any number divides candidate, i.e. not prime
            flag = 1
            break
        divisor = divisor + 1 #else, update divisor
    if flag == 0: #if prime, update count
        count = count + 1
    if count < 1000:
        candidate = candidate + 2 #do not update after count = 1000, else 
                                  #we get wrong answer

if count == 1000:   #just a sanity check
    print '1000th prime is', candidate        
    
# 1000th prime = 7919 - verified
