file = open('demofile.txt','r')
# print(file.read())

print()
print(file.read(5))
print(file.readline())
print(file.readline())

for x in file:
  print(x)
# file.close()

# print(file.read())