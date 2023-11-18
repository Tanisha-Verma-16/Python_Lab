i = 1
j = 0
while j <= 100:
    j = j + 2 * i
    i += 1
    if j > 100:
        break
    print(j, end = ',')
    