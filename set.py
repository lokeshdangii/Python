star = {2,4,6,2, "Yes", "No", 2.4, 11,5+1j}

star.add("Lokesh")
print(star)

#star.pop() #random value will pop
#print(star)

# star.remove("Yes") # will take element as parameter not index..!!
# print(star)

#star.clear()

# remove() will give error if argument doesn't exist

star.discard(6)  #discard will not give error if elemet not exist
print(star)


