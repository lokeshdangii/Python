import random
list1 = []

for i in range(1,101):
    list1.append(i)

list2 = []
for i in range(0,10):
    ele = random.choice(list1)
    list2.append(ele)
    # list1.remove(ele)

set1 = set(list2)

if len(set1)<10:
    length = len(set1)
    while length==10:
        item = random.choice(list1)
        set1.add(item)
        length = length + 1
else:
    pass
    
print("The ten elements are : ",set1)

    
