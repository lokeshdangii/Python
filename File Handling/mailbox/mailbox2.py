'''
10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below.
'''
# opening the file in read mode in file variable
file = open("mbox-short.txt","r")
# print(file.read())

# storing its text in data
data = file.read()

# closing the after its work is completed
file.close()

# splitting the textual data by word ("From ") and storing in list record
record = data.split("From ")

# declaring en empty list to store the specific time at which mail has sent
hour_list = []

# for loop to split the text of ever element of the record list and storing in a time[] list
for i in range(1,len(record)):
    time = record[i].split()
    # storing the value of 5th index of time list in hour as the 5th index is holding the time at which mail has sent
    hour = time[4]
    hour_list.append(hour) # appending the extracted time in hour list

# sorting the list in increasing order
hour_list.sort()

# printing the hour list 
print(hour_list)
