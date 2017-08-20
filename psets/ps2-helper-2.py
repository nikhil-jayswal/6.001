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
