def sum(l):
    sum = 1
    for i in l:
        sum *= i 
    return sum

l1 = [23,56,78,4,52]
print(sum(l1))