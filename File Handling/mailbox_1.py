'''
Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. The program looks for 'From '
lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to
a count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop
to find the most prolific committer.
'''

file = open("mbox-short.txt", "r")
# print(file.read())

data = file.read()
record = data.split("From ")

dict1 = {}
list1 = []

for i in range(0,len(record)):
    text = record[i].split()
    name = text[0]
    list1.append(name)


# print(list1)

for i in range(1,len(list1)):
    count = 0
    for j in range(0,len(list1)):
        if list1[i] == list1[j]:
            count = count+1

    dict1.update({list1[i]:count})
    



print(dict1)
print()
max_count = max(dict1.values())

for key, value in dict1.items():
        if value == max_count:
            print(f"Name : {key}, Mail_Count : {value}")

    
file.close()


