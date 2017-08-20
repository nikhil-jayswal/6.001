numCalls = 0

def func1():
    Memo = {}
    func2(Memo)
    return Memo 

def func2(Memo):
    # this statement is telling the function to use the global numCalls variable
    global numCalls
    numCalls += 1
    Memo['1'] = 'One'
    return None

print func1()
print numCalls


