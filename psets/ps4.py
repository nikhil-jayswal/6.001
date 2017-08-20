# Problem Set 4
# Name: Nikhil Jayswal

#
# Problem 1
#

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    
    # verify if inputs are valid
    assert salary >= 0, 'Salary must be non-negative'
    assert save >= 0 and save <= 100, 'Save percentage must be between 0 and 100'
    assert growthRate >= 0 and growthRate <= 100, 'Growth Rate percentage must be between 0 and 100'
    assert years > 0 and type(years) == type(0), 'Number of years to work must be positive integer'
    
    
    # define a variable with value equal to F[0]
    value = salary * save * 0.01 
    # round to nearest penny
    value = round(value, 2)
    
    # base case for recursive procedure
    if years == 1:
        return [value, ]
    
    # recursive step
    else: 
        
        # get retirement account details from today till the end of previous year
        prev = nestEggFixed(salary, save, growthRate, years - 1)
        
        # calculate size of retirement account for this year
        temp = prev[-1] * (1 + 0.01 * growthRate) + value
        # round to nearest penny
        temp = round(temp, 2)
        
        # append calculated value
        prev = prev + [temp, ]
        
        #return answer
        return prev

    
def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    salary     = 12000
    save       = 9.5
    growthRate = 0
    years      = 2
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord

# Uncomment the line below to test nestEggFixed()
#testNestEggFixed()

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRates: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    # verify if inputs are valid
    assert salary >= 0, 'Salary must be positive'
    assert save >= 0 and save <= 100, 'Save percentage must be between 0 and 100'
    
    flag = 0
    for var in growthRates:
        if var < 0 or var > 100:
            flag = 1
            break
    
    assert flag == 0, 'Growth Rate percentages must be between 0 and 100'

    # get number of years to work
    years = len(growthRates)
        
    # define a variable with value equal to F[0]
    value = salary * save * 0.01 
    # round to nearest penny
    value = round(value, 2)
    
    # base case for recursive procedure
    if years == 1:
        return [value, ]
    
    # recursive step
    else: 
        
        # get retirement account details from today till the end of previous year
        prev = nestEggVariable(salary, save, growthRates[:-1])
        
        # calculate size of retirement account for this year
        temp = prev[-1] * (1 + 0.01 * growthRates[-1]) + value
        # round to nearest penny
        temp = round(temp, 2)
        
        # append calculated value
        prev = prev + [temp, ]
        
        #return answer
        return prev

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    salary      = 10000
    save        = 8.5
    growthRates = [3, 4, 5, 0.5, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    
# Uncomment the line below to test nestEggVariable()
#testNestEggVariable()

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # verify if inputs are valid
    assert savings >= 0, 'Savings must be non-negative'
    assert expenses >= 0, 'Expenses must be non-negative'
    
    flag = 0
    for var in growthRates:
        if var < 0 or var > 100:
            flag = 1
            break
    
    assert flag == 0, 'Growth Rate percentages must be between 0 and 100'
    
    # calculate number of years of expenditure
    years = len(growthRates)
    
    # base case for recursive procedure
    if years == 1:
        value = savings * (1 + 0.01 * growthRates[0]) - expenses
        
        # round to nearest penny
        value = round(value, 2)
        
        return [value, ]
    
    # recursive step
    else: 
        
        # get retirement account details from today till the end of previous year
        prev = postRetirement(savings, growthRates[:-1], expenses)
        
        # calculate size of retirement account for this year
        temp = prev[-1] * (1 + 0.01 * growthRates[-1]) - expenses
        # round to nearest penny
        temp = round(temp, 2)
        
        # append calculated value
        prev = prev + [temp, ]
        
        #return answer
        return prev

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]
    
    savings     = 125000
    growthRates = [10, 5, 0.5, 5, 1]
    expenses    = 30000.50
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

# Uncomment the following line to test postRetirement()
#testPostRetirement()

#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # verify if inputs are valid
    assert salary >= 0, 'Salary must be non-negative'
    assert save >= 0 and save <= 100, 'Save percentage must be between 0 and 100'
        
    flag = 0
    for var in preRetireGrowthRates:
        if var < 0 or var > 100:
            flag = 1
            break
    
    assert flag == 0, 'Growth Rate percentages must be between 0 and 100'
    
    flag = 0
    for var in postRetireGrowthRates:
        if var < 0 or var > 100:
            flag = 1
            break
    
    assert flag == 0, 'Growth Rate percentages must be between 0 and 100'
    
    assert epsilon > 0, 'epsilon must be positive'

    # calculate number of working and retirement years    
    workingYears = len(preRetireGrowthRates)
    retirementYears = len(postRetireGrowthRates)
    
    # initial estimates for upper and lower bounds
    # lower bound = 0
    low = 0
    # higher bound = savings at the end of working years 
    savings = nestEggVariable(salary, save, preRetireGrowthRates)
    high = savings[-1]
              
    # counter for number of iterations
    ctr = 1
    while(True):
        
        # calculate estimate for post retirement expenses
        estimate = (low + high) / 2.0
        
        print 'Iteration #:', ctr
        print 'Estimate is:', estimate
        
        # calculate money left at the end of retirement years
        temp = postRetirement(savings[-1], postRetireGrowthRates, estimate)
        moneyLeft = temp[-1]
        
        # if money remaining or debt at the end is more than allowed
        # revise estimates of higher and lower bounds
        if abs(moneyLeft) > epsilon:
            # if money remains, revise low estimate
            if moneyLeft > 0: low = estimate
            # if in debt, revise high estimate
            elif moneyLeft < 0: high = estimate
        
        # else, exit loop
        else : break
        
        # update counter
        ctr = ctr + 1
           
    # return estimate rounded to nearest penny
    estimate = round(estimate, 2)
    return estimate

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print 'Max Expenses:', expenses
    # Output should have a value close to:
    # 1229.95548986

# Uncomment the following line to test findMaxExpenses()
testFindMaxExpenses()
# Comment the round statements to get answer = 1229.95548986 
