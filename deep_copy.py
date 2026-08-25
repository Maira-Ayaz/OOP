'''import copy
str = ["maira"]
str1 = copy.deepcopy(str)
str1.append("ayaz")
print(str1)#copied 
print(str)'''

import copy

list1 = [["Maira"], ["Ayaz"]]

list2 = copy.deepcopy(list1)

list2[0].append("CS")

print("list1:", list1)
print("list2:", list2)
