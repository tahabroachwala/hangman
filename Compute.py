def function(k):
    calc = ((pow(-1, k + 1)) / ((2*k) - 1))
    return calc
list1 = []
for i in range(0, pow(10, 6) + 1):
    funcCatch = function(i)
    list1.append(funcCatch)
print(list1)
finalCalc = 4 * sum(list1)
print(finalCalc)