print('The numbers divisible by 7 which are also multiples of 5 are :')
list1 = []
for i in range(1500,2701):
    if i % 5 == 0 and i % 7 == 0:
        list1.append(i)

print(list1)