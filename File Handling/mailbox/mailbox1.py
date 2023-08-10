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

# storing the file text in data
data = file.read()
file.close()
# closing file

# splitting the text by the word "From" and storing output in list record
record = data.split("From ")

name_count = {}
name_list = []

# for loop to split the text of ever element of the record list and storing in a text list 
for i in range(0,len(record)):
    text = record[i].split()
    name = text[0] #storing the first word from the text[] which is a name of the person who mail
    name_list.append(name) # and appending the in name list

print(name_list) #print the names from the name_list

# for loop to count how many times a name occurs and storing in a dictionary
for i in range(1,len(name_list)):
    count = 0
    for j in range(0,len(name_list)):
        if name_list[i] == name_list[j]:
            count = count+1

    name_count.update({name_list[i]:count}) #key:value pair --> name:count
    

print(name_count)  #prints the name and respective count of how many time name occurs
print() #next line


max_count = max(name_count.values()) # storing the maximum count 

# for loop to check and print which person have send mail most number of time
for key, value in name_count.items():
        if value == max_count:  
            print(f"Name : {key}, Mail_Count : {value}") 



