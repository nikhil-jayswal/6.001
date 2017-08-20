# Problem Set 1b
# Nikhil Jayswal
#
# Computing sum of logarithms of all primes from 2 to n
#
from math import * #import math to compute logarithms
n = int(raw_input('Enter a number (greater than 2): '))

start = 3 #the second prime; don't need this can do candidate = 3
log_sum = log(2) #sum of logarithms of primes, first prime is 2
candidate = start

while (candidate <= n): #upto n
    divisor = 2 
    flag = 0   
    while (divisor < candidate):
        if (candidate % divisor == 0): #if any number divides candidate, i.e.not prime
            flag = 1
            break
        divisor = divisor + 1 #else, update divisor
    if flag == 0: #if prime, update log_sum
        log_sum += log(candidate) 
    candidate = candidate + 2 #update candidate

ratio = log_sum / n #log_sum should be float, hence division should be proper

print 'n = ', n
print 'Sum of logarithms of primes upto', n, 'is', log_sum
print 'Ratio of sum of logarithm of primes to n is', ratio

# Code works but results not verified
