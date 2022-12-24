numdict={}
for i in range(1,100):
    count = 0
    for j in range(2,i+1):
        if (i%j)==0:
            count+=1
    numdict[i] = count

#print(numdict)

k = list(numdict.keys())
v = list(numdict.values())

valuemax = max(v)
print("maximum value of divisor:",valuemax) 


for x, y in numdict.items():
  if y == valuemax:
    print("The number which have maximum divisor is :",x)