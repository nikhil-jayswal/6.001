Nuggets = int(raw_input('Enter the amount of McNuggets: '))

#solve by exhaustive enumeration
CountSix = 0
CountNine = 0
CountTwenty = 0

MaxSix = (Nuggets / 6) + 1
MaxNine = ((Nuggets - 6 * CountSix) / 9) + 1
MaxTwenty = ((Nuggets - 6 * CountSix - 9 * CountNine) / 20) + 1

solutions = ()

#flag = 0
#for CountSix in range(0, MaxSix):
#    for CountNine in range (0, MaxNine):
#        for CountTwenty in range (0, MaxTwenty):
#            Total = 6 * CountSix + 9 * CountNine + 20 * CountTwenty
#            if Total == Nuggets:
#                flag = 1
#                print 'Number of 6 packets -', CountSix
#                print 'Number of 9 packets -', CountNine
#                print 'Number of 20 packets -', CountTwenty
#                break
#        if flag == 1:
#            break
#    if flag == 1:
#        break
#
#if flag == 0:
#    print 'No solution found!'

#for multiple solutions
for CountSix in range(0, MaxSix):
    for CountNine in range (0, MaxNine):
        for CountTwenty in range (0, MaxTwenty):
            Total = 6 * CountSix + 9 * CountNine + 20 * CountTwenty
            if Total == Nuggets:
                solutions += ((CountSix, CountNine, CountTwenty),)
print solutions
                  
                  

    

