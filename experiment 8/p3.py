j = 0
i = 66
while i > 0:
    if j%2 == 0:
        i = i - 13
    else:
        i = i 
    j += 1 
    if i > 0:
        print(i, end = ",")