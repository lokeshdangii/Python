l1 =[10,20,30]
l2 = l1[:]

t1 = (10,20,30)
t2 = t1[:]


s1 = "Prabhas"
s2 = s1[:]


print(l1 is l2)  # false b
print(t1 is t2)
print(s1 is s2)