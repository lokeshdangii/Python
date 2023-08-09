import random
list1 = []

for i in range(1,101):
    list1.append(i)

ele = random.choice(list1)
set1 = {ele}

for i in range(0,8):
    ele= random.choice(list1)
    set1.add(ele)

while(len(set1)<10):
    ele= random.choice(list1)
    set1.add(ele)

print(set1)