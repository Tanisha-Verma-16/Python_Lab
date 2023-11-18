def distinct():
    n = input("Input ")
    l = n.split()
    l1 = []
    for i in range(len(l)):
        if l[i] not in l1:
            
            l1.append(l[i])
    print("Output : ",end = "")
    for i in l1:
        print(i,end=" ")
    

distinct()