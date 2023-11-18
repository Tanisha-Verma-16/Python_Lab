j = 0
i = 9
while i <= 50:
    if j%2 == 0:
        i = i -2
    else:
        i = i + 3
    j += 1 
    print(i, end = ",")