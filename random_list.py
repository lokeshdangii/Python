import random
list1 = []

for i in range(1,101):
    list1.append(i)

list2 = []
for i in range(0,10):
    ele = random.choice(list1)
    list2.append(ele)
    list1.remove(ele)

print("The ten elements are : ",list2)

    
