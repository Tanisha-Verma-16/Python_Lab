dict1 = {1:'jan',2:'feb',3:'mar'}
dict2 = {4:'apr', 5:'may', 6:'jun'}

dict_merged = {**dict1,**dict2}
print(dict1)
print(dict2)
print("Merged dictionary : ",dict_merged)