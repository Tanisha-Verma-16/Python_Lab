list1 = [3, 64, 32, 12, 55, 8]
for i in range(len(list1)):
    if list1[0] < list1[i]:
        list1[0], list1[i] = list1[i], list1[0]
print(f'Maximum value is {list1[0]}')
print(list1)
