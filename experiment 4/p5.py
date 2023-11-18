def list_compare(l1,l2):
    if l1 == l2:
        print("Lists are equal")

    else:
        if len(l1) == len(l2):
            for i in range(len(l1)):
                if l1[i] == l2[i]:
                    print(f"Items at {i} index are equal")
                else:
                    print(f"Items at {i} index are not equal")
        else:
            print("List length not equal")

l1 = [10,20,30,40,50]
l2 = [50,60,70,80,50]
l3 = [10,20,30,40,50]
l4 = [10,20]

list_compare(l1,l2)
