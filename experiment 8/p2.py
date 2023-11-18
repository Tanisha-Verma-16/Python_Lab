j = 0
i = 20
while i <= 80:
    if j%2 == 0:
        i = i + 2
    else:
        i = i - 1
    j += 1 
    print(i, end = ",")