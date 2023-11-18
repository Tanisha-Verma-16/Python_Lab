def num_pall(n):
    str1 = ''
    for i in range(1,n+1):
        if i < n:
            str1 += str(i)
        elif i == n :
            for j in range(n,0,-1):
                str1 += str(j)
    return str1


for i in range(1,6):
    print(' '*(5-i) + num_pall(i))
