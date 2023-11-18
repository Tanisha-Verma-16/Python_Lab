key = int(input("Enter the key to be checked : "))
dict = {1:'jan',2:'feb',3:'mar'}
keys = dict.keys()
if key in keys:
    result = dict[key]
    print("Key exists_", key, ":", result)
else:
    print("Key does not exist")