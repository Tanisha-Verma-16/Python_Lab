def max_num(a,b,c):
    l1 = [a,b,c]
    i = 0
    while i < len(l1) - 1:
        if l1[i] > l1[i+1]:
            l1[i], l1[i+1] = l1[i+1], l1[i]
        i += 1

    return l1[len(l1)-1]

print(max_num(809,4,9))
