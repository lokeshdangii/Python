# n = int(input("Enter value:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end =" ")
#     print("\r")   


n = 5
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end = " ")
    print("\r")