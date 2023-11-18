def count_int():
    n = input("Enter the list")
    l = n.split()
    l1 = []
    for i in range(len(l)):
        if l[i] not in l1:
            count = 0
            for j in range(len(l)):
                if l[i] == l[j]:
                    count += 1
            l1.append(l[i])
            print(f"{l[i]} occurs {count} times")

count_int()