j = 0
i = 22
while i <= 100:
    if j%2 == 0:
        i = i - 8
    else:
        i = i * 2
    j += 1 
    print(i, end = ",")